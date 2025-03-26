"""
Gemini-based multi-agent implementation for test harness.
A simplified test to validate Gemini API connectivity and sequential task workflow.
"""
from crewai import Agent, Task, Crew, Process
import google.generativeai as genai
import os
import logging
import json
from typing import Any, List, Optional, Dict
from pydantic import PrivateAttr # For non-validated private attributes if needed
from pydantic_core import PydanticCustomError # If needed for custom validation
from dotenv import load_dotenv
from src.ollama.tools.tool_factory import ToolFactory
from src.ollama.simplified_agents import get_gemini_agents
from src.ollama.simplified_tasks import get_sequential_tasks
from src.ollama.knowledge.manager import KnowledgeManager
from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM
from langchain_core.outputs import GenerationChunk, Generation, LLMResult



# Load environment variables if needed
# load_dotenv()

# Setup basic logging if desired
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

class GeminiChatLLM(LLM):
    """
    Custom LangChain LLM wrapper for Google Gemini models using google-generativeai.

    Uses Pydantic v2 model_post_init for client setup after config validation.
    """

    # --- Configuration parameters declared as class attributes ---
    # Pydantic will validate these and use os.getenv for defaults.
    model_name: str = os.getenv("GEMINI_MODEL", "gemini-1.5-pro-latest")
    temperature: float = float(os.getenv("GEMINI_TEMPERATURE", 0.7))
    top_p: float = float(os.getenv("GEMINI_TOP_P", 1.0))
    # top_k: Optional[int] = os.getenv("GEMINI_TOP_K") # Add if needed
    max_output_tokens: int = int(os.getenv("GEMINI_MAX_TOKENS", 8192))

    # --- Safety Settings (Class attribute for consistency) ---
    safety_settings: Dict[str, str] = {
        "HARM_CATEGORY_HARASSMENT": "BLOCK_NONE",
        "HARM_CATEGORY_HATE_SPEECH": "BLOCK_NONE",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT": "BLOCK_NONE",
        "HARM_CATEGORY_DANGEROUS_CONTENT": "BLOCK_NONE",
    }

    # --- Internal client instance ---
    # Make it a private attribute so Pydantic doesn't treat it as a model field
    # We will initialize it in model_post_init
    _client: Any = PrivateAttr(default=None)

    # --- REMOVED custom __init__ ---
    # Let Pydantic handle initialization of model_name, temperature etc.

    def model_post_init(self, __context: Any) -> None:
        """
        Initialize the google.generativeai client after Pydantic validation.
        This method is called automatically by Pydantic v2 after __init__.
        """
        # Get API key from environment
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            # logger.error("GEMINI_API_KEY environment variable not set")
            raise ValueError("GEMINI_API_KEY environment variable not set")

        try:
            # Configure the Gemini API client library
            genai.configure(api_key=api_key)

            # Prepare generation config from validated class attributes
            generation_config = genai.types.GenerationConfig(
                temperature=self.temperature,
                top_p=self.top_p,
                # top_k=self.top_k, # Add if configured
                max_output_tokens=self.max_output_tokens,
                candidate_count=1
            )

            # Initialize the generative model client instance and store it
            self._client = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=generation_config,
                safety_settings=self.safety_settings
            )
            # logger.info(f"Gemini client initialized for model: {self.model_name}")
        except Exception as e:
            # logger.exception("Failed to initialize Gemini client in model_post_init")
            raise ValueError(f"Failed to initialize Gemini client: {e}") from e

    # --- Getter for the client to use in methods ---
    @property
    def client(self) -> Any:
        """Get the initialized GenerativeModel client."""
        if self._client is None:
             # This should not happen if model_post_init ran correctly
             raise ValueError("Gemini client not initialized. model_post_init may have failed.")
        return self._client


    @property
    def _llm_type(self) -> str:
        """Return identifier for this LLM type."""
        return "gemini-chat"

    def _get_generation_config(self, stop: Optional[List[str]] = None, **kwargs: Any) -> genai.types.GenerationConfig:
        """
        Helper to create GenerationConfig, merging instance defaults with runtime options.
        """
        config_dict = {
            "temperature": self.temperature, "top_p": self.top_p,
            "max_output_tokens": self.max_output_tokens, "candidate_count": 1
        }
        if stop: config_dict["stop_sequences"] = stop
        allowed_runtime_keys = ["temperature", "top_p", "top_k", "max_output_tokens", "candidate_count", "stop_sequences"]
        for key, value in kwargs.items():
            if key in allowed_runtime_keys: config_dict[key] = value
        # Ensure correct types if necessary
        if "max_output_tokens" in config_dict: config_dict["max_output_tokens"] = int(config_dict["max_output_tokens"])
        if "candidate_count" in config_dict: config_dict["candidate_count"] = int(config_dict["candidate_count"])

        return genai.types.GenerationConfig(**config_dict)

    def _handle_gemini_response(self, response: genai.types.GenerateContentResponse) -> str:
        """Safely extracts text from the Gemini response, handling potential errors/blocks."""
        try:
            if hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
                raise ValueError(f"Gemini API blocked prompt. Reason: {response.prompt_feedback.block_reason}")
            if response.candidates:
                candidate = response.candidates[0]
                if candidate.finish_reason == "SAFETY":
                    safety_ratings_str = ""
                    if hasattr(candidate, 'safety_ratings') and candidate.safety_ratings:
                        safety_ratings_str = ", ".join([f"{rating.category.name}: {rating.probability.name}" for rating in candidate.safety_ratings])
                    raise ValueError(f"Gemini API blocked response due to safety settings. Finish Reason: SAFETY. Ratings: [{safety_ratings_str}]")
                elif candidate.finish_reason not in ["STOP", "MAX_TOKENS"]:
                     raise ValueError(f"Gemini API finished with unexpected reason: {candidate.finish_reason}")
                if hasattr(candidate, 'content') and candidate.content and hasattr(candidate.content, 'parts') and candidate.content.parts:
                    return "".join(part.text for part in candidate.content.parts if hasattr(part, 'text'))
                else: return "" # Finished normally but no content
            else:
                 if hasattr(response, 'prompt_feedback') and response.prompt_feedback.block_reason:
                     raise ValueError(f"Invalid Gemini response: No candidates found. Prompt blocked. Reason: {response.prompt_feedback.block_reason}")
                 else: raise ValueError("Invalid Gemini response: No candidates found and prompt not blocked.")
        except Exception as e: raise e # Re-raise

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        """Execute a single call to the Gemini model."""
        # Use the client property getter
        client = self.client
        llm_output = {}
        try:
            generation_config = self._get_generation_config(stop=stop, **kwargs)
            if run_manager:
                run_manager.on_llm_start({}, [prompt], invocation_params=self._identifying_params)
            response = client.generate_content(prompt, generation_config=generation_config)
            result_text = self._handle_gemini_response(response)
            if hasattr(response, 'usage_metadata'):
                 llm_output["token_usage"] = {
                     "prompt_token_count": response.usage_metadata.prompt_token_count,
                     "candidates_token_count": response.usage_metadata.candidates_token_count,
                     "total_token_count": response.usage_metadata.total_token_count,
                 }
                 llm_output["usage_metadata"] = response.usage_metadata
            if run_manager:
                generation = Generation(text=result_text)
                run_manager.on_llm_end(LLMResult(generations=[[generation]], llm_output=llm_output))
            return result_text
        except Exception as e:
            if run_manager:
                run_manager.on_llm_error(e, response=LLMResult(generations=[], llm_output=llm_output))
            raise e # Re-raise

    # --- Streaming method (Optional) ---
    # def _stream(...) -> Iterator[GenerationChunk]: ... (Implement as before if needed)

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """Get the identifying parameters for LangChain callbacks and caching."""
        return {
            "model_name": self.model_name, "temperature": self.temperature,
            "top_p": self.top_p, "max_output_tokens": self.max_output_tokens,
        }

# --- Example Usage (Optional - place in your main script) ---
# if __name__ == "__main__":
#     load_dotenv() # Ensure environment variables are loaded
#     try:
#         gemini_llm = GeminiChatLLM()
#         print("Gemini LLM Initialized Successfully.")
#         prompt = "Explain the difference between LangChain and CrewAI in simple terms."
#         print(f"\nSending prompt: {prompt}\n")
#         response_text = gemini_llm.invoke(prompt)
#         print("--- Response ---")
#         print(response_text)
#         print("----------------")
#     except ValueError as ve: print(f"Error: {ve}")
#     except Exception as e: print(f"An unexpected error occurred: {e}")

    @property
    def _identifying_params(self) -> Dict[str, Any]:
        """
        Get the identifying parameters for LangChain callbacks and caching.
        Includes parameters defined in the class and affects hashing.
        """
        return {
            "model_name": self.model_name,
            "temperature": self.temperature,
            "top_p": self.top_p,
            # "top_k": self.top_k, # Add if configured
            "max_output_tokens": self.max_output_tokens,
            # Include safety_settings if they significantly alter behavior and should be part of the identity
            # "safety_settings": self.safety_settings
        }

# --- Example Usage (Optional - place in your main script) ---
# if __name__ == "__main__":
#     load_dotenv() # Ensure environment variables are loaded
#
#     try:
#         gemini_llm = GeminiChatLLM()
#         print("Gemini LLM Initialized Successfully.")
#
#         prompt = "Explain the difference between LangChain and CrewAI in simple terms."
#         print(f"\nSending prompt: {prompt}\n")
#
#         # Simple call
#         response_text = gemini_llm.invoke(prompt)
#         print("--- Response ---")
#         print(response_text)
#         print("----------------")
#
#         # Example with stop sequence
#         # response_with_stop = gemini_llm.invoke(prompt, stop=["CrewAI"])
#         # print("\n--- Response with stop sequence ---")
#         # print(response_with_stop)
#         # print("--------------------------------")
#
#         # Example streaming call (uncomment _stream method first)
#         # print("\n--- Streaming Response ---")
#         # for chunk in gemini_llm.stream(prompt):
#         #     print(chunk, end="", flush=True)
#         # print("\n------------------------")
#
#
#     except ValueError as ve:
#         print(f"Configuration Error: {ve}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

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
                    self.knowledge_manager.store_entry("reports", entry_id, parsed_content)
                    return f"Successfully saved structured report to knowledge base with ID: {entry_id}"
                except json.JSONDecodeError:
                    # If not valid JSON, save as raw text
                    entry_id = f"report_{self.topic.replace(' ', '_')}"
                    self.knowledge_manager.store_entry("reports", entry_id, {"content": content, "topic": self.topic})
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
            verbose=1,  # Maximum verbosity since update
            process=Process.sequential  # Ensure sequential execution
        )

        # Execute the crew
        result = crew.kickoff()

        self.logger.info("GeminiMultiCrew execution completed")
        return result
