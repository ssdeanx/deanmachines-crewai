"""
Gemini-based multi-agent implementation for test harness.
A simplified test to validate Gemini API connectivity and sequential task workflow.
"""
from crewai import Agent, Task, Crew, Process
import google.generativeai as genai  # Updated import for Gemini 2.0
import os
import logging
import json
from typing import Any, List, Optional, Dict
from dotenv import load_dotenv
from src.ollama.tools.tool_factory import ToolFactory
from src.ollama.simplified_agents import get_gemini_agents
from src.ollama.simplified_tasks import get_sequential_tasks
from src.ollama.knowledge.manager import KnowledgeManager
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM

# Load environment variables at module level
load_dotenv()

class GeminiChatLLM(LLM):
    """Custom LangChain wrapper for Gemini 2.0 using the updated google.generativeai library."""

    def __init__(self, **kwargs):
        """Initialize the Gemini LLM with API key and configure genai."""
        super().__init__(**kwargs)

        # Get API key from environment
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")

        # Configure the Gemini API
        genai.configure(api_key=api_key)

        # Load all configuration from environment variables
        self.model_name = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
        self.temperature = float(os.getenv("GEMINI_TEMPERATURE", "0.7"))
        self.top_p = float(os.getenv("GEMINI_TOP_P", "0.95"))
        self.max_output_tokens = int(os.getenv("GEMINI_MAX_TOKENS", "2048"))
        self.context_window = int(os.getenv("GEMINI_CONTEXT_WINDOW", "1000000"))

        # Override defaults with any provided kwargs
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

        # Initialize the model with proper configuration
        generation_config = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "max_output_tokens": self.max_output_tokens
        }

        safety_settings = {
            "harassment": "block_none",
            "hate_speech": "block_none",
            "sexually_explicit": "block_none",
            "dangerous_content": "block_none"
        }

        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=generation_config,
            safety_settings=safety_settings
        )

    @property
    def _llm_type(self) -> str:
        """Return the type of LLM."""
        return "gemini"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """
        Call the Gemini API and return the response.

        Args:
            prompt: The input text to send to the model
            stop: Optional list of stop sequences to end generation
            run_manager: Optional callback manager for logging
            **kwargs: Additional keyword arguments passed to the model

        Returns:
            The generated text response

        Raises:
            ValueError: If there's an error calling the Gemini API
        """
        try:
            # If we have a run_manager, use it to log the prompt
            if run_manager:
                run_manager.on_text(prompt, color="green", end="\n")

            # Generate the response
            response = self.model.generate_content(
                prompt,
                generation_config=self._get_generation_config(stop=stop, **kwargs)
            )

            # Handle potential errors in the response
            if not response:
                raise ValueError("Empty response from Gemini API")

            if response.error:
                raise ValueError(f"Gemini API error: {response.error}")

            # Extract the text from the response
            result = response.text

            # Apply stop sequences if provided
            if stop:
                for sequence in stop:
                    if sequence in result:
                        result = result[:result.index(sequence)]

            # Log the response if we have a run_manager
            if run_manager:
                run_manager.on_text(result, color="blue", end="\n")

            return result

        except Exception as e:
            error_msg = f"Error calling Gemini API: {str(e)}"
            if run_manager:
                run_manager.on_text(error_msg, color="red", end="\n")
            raise ValueError(error_msg)

    def _get_generation_config(self, stop: Optional[List[str]] = None, **kwargs) -> Dict[str, Any]:
        """
        Create a generation config dict combining instance defaults with call-specific params.

        Args:
            stop: Optional list of stop sequences
            **kwargs: Additional keyword arguments to override defaults

        Returns:
            Dict with generation configuration parameters
        """
        config = {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "max_output_tokens": self.max_output_tokens,
            "candidate_count": 1
        }

        # Override with any valid kwargs
        valid_params = ["temperature", "top_p", "max_output_tokens", "candidate_count"]
        for param in valid_params:
            if param in kwargs:
                config[param] = kwargs[param]

        return config

class GeminiMultiCrew:
    """
    A simplified CrewAI implementation using only Gemini for all agents.
    This test harness validates:
    1. Gemini API connectivity
    2. Basic CrewAI sequential task execution
    3. Context passing between tasks
    4. Basic ToolFactory operation with web_search
    5. Knowledge base writing from the reporter agent
    """

    def __init__(self, topic="climate change impacts on agriculture"):
        """
        Initialize the GeminiMultiCrew.

        Args:
            topic: The topic to research, summarize, and report on
        """
        self.topic = topic
        self.logger = logging.getLogger(__name__)

        # Initialize Gemini 2.0 LLM with proper configuration from environment
        try:
            self.gemini_llm = GeminiChatLLM()  # Will raise ValueError if GEMINI_API_KEY not set
            self.logger.info(f"Successfully initialized Gemini 2.0 LLM with model: {self.gemini_llm.model_name}")
        except Exception as e:
            self.logger.error(f"Failed to initialize Gemini LLM: {e}")
            raise

        # Initialize Knowledge Manager for storing results
        try:
            self.knowledge_manager = KnowledgeManager()
            self.logger.info("Successfully initialized KnowledgeManager")
        except Exception as e:
            self.logger.warning(f"Failed to initialize KnowledgeManager: {e}")
            self.knowledge_manager = None

        # Initialize ToolFactory and try to get web_search tool
        self.tool_factory = ToolFactory()
        self.web_search_tool = None
        try:
            self.web_search_tool = self.tool_factory.get_tool("web_search")
            self.logger.info("Successfully initialized web_search tool")
        except (KeyError, Exception) as e:
            self.logger.warning(f"Failed to initialize web_search tool: {e}. This might be due to missing SERPER_API_KEY.")

        # Initialize agents and tasks
        self._create_agents_and_tasks()

    def _create_agents_and_tasks(self):
        """
        Create all agents and tasks for the crew.
        All agents use the Gemini LLM. Only the researcher gets the web_search tool.
        Tasks are set up with proper context=[previous_task] linking.
        """
        # Prepare tools
        tools = {}
        if self.web_search_tool:
            tools["researcher"] = [self.web_search_tool]

        # Create knowledge saving tool for the reporter
        if self.knowledge_manager:
            try:
                knowledge_save_tool = self._create_knowledge_save_tool()
                tools["reporter"] = [knowledge_save_tool]
                self.logger.info("Successfully created knowledge save tool for reporter")
            except Exception as e:
                self.logger.warning(f"Failed to create knowledge save tool: {e}")

        # Create agents
        self.agents = get_gemini_agents(self.gemini_llm, tools)
        self.logger.info("Successfully created Gemini agents")

        # Create tasks with proper context passing
        self.tasks = get_sequential_tasks(self.agents, self.topic)
        self.logger.info("Successfully created sequential tasks")

    def _create_knowledge_save_tool(self):
        """
        Create a tool for the reporter agent to save results to the knowledge base.

        Returns:
            A tool instance for saving content to the knowledge base
        """
        from langchain.tools import Tool

        def save_to_knowledge(content):
            """
            Save the provided content to the knowledge base.

            Args:
                content: The content to save, either as a string or a JSON string

            Returns:
                Confirmation message of successful saving
            """
            try:
                # Try to parse as JSON if it's structured
                try:
                    parsed_content = json.loads(content)
                    entry_id = f"report_{self.topic.replace(' ', '_')}"
                    self.knowledge_manager.save_entry("reports", entry_id, parsed_content)
                    return f"Successfully saved structured report to knowledge base with ID: {entry_id}"
                except json.JSONDecodeError:
                    # If not valid JSON, save as raw text
                    entry_id = f"report_{self.topic.replace(' ', '_')}"
                    self.knowledge_manager.save_entry("reports", entry_id, {"content": content, "topic": self.topic})
                    return f"Successfully saved text report to knowledge base with ID: {entry_id}"
            except Exception as e:
                return f"Error saving to knowledge base: {str(e)}"

        return Tool(
            name="save_to_knowledge",
            description="Save your final report to the knowledge base for future reference. You should use this tool at the end of your report to store your findings. The content should be your complete report.",
            func=save_to_knowledge
        )

    def run(self):
        """
        Execute the crew with sequential task processing.

        Returns:
            The final result from the crew execution
        """
        self.logger.info(f"Starting GeminiMultiCrew execution for topic: {self.topic}")

        # Create and configure the crew
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=self.tasks,
            verbose=2,  # Maximum verbosity for detailed logging
            process=Process.sequential  # Ensure sequential execution
        )

        # Execute the crew
        result = crew.kickoff()

        self.logger.info("GeminiMultiCrew execution completed")
        return result
