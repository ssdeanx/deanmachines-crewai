"""
Gemini-based multi-agent implementation for test harness.
A simplified test to validate Gemini API connectivity and sequential task workflow.
"""
from crewai import Agent, Task, Crew, Process
import google.generativeai as genai  # Updated import for Gemini 2.0
import os
import logging
import json
from dotenv import load_dotenv
from src.ollama.tools.tool_factory import ToolFactory
from src.ollama.simplified_agents import get_gemini_agents
from src.ollama.simplified_tasks import get_sequential_tasks
from src.ollama.knowledge.manager import KnowledgeManager
from langchain.schema.language_model import BaseLanguageModel
from langchain_core.language_models.llms import LLM
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from typing import Any, List, Mapping, Optional

class GeminiChatLLM(LLM):
    """Custom LangChain wrapper for Gemini 2.0 using the updated google.generativeai library."""

    model_name: str = "gemini-1.5-pro"
    temperature: float = 0.7
    top_p: float = 0.95
    top_k: int = 0

    def __init__(self, api_key: str, **kwargs):
        """Initialize the Gemini LLM with API key and configure genai."""
        super().__init__(**kwargs)
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(model_name=self.model_name,
                                          generation_config={
                                              "temperature": self.temperature,
                                              "top_p": self.top_p,
                                              "top_k": self.top_k
                                          })

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
        """Call the Gemini API and return the response."""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise ValueError(f"Error calling Gemini API: {e}")

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

        # Check for required API key
        gemini_api_key = os.getenv("GEMINI_API_KEY")
        if not gemini_api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set")

        # Initialize Gemini 2.0 LLM with the new google.generativeai library
        self.gemini_llm = GeminiChatLLM(
            api_key=gemini_api_key,
            model_name=os.getenv("GEMINI_MODEL", "gemini-1.5-pro"),
            temperature=0.7
        )

        self.logger.info("Successfully initialized Gemini 2.0 LLM")

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
