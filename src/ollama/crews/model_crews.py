from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew, LLM
import os
from pathlib import Path
from datetime import datetime
import json
from ..tools.search_tools import SearchManager
import logging
from ..tools.tool_factory import ToolFactory

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)

class BaseModelCrew:
    def __init__(self, topic: str = "AI and machine learning"):
        self.topic = topic
        self.agents = {}
        self.output_dir = Path("./outputs")
        self.output_dir.mkdir(exist_ok=True)
        self.tool_factory = ToolFactory()
        self.llm = self._setup_llm()
        self.search_manager = SearchManager()

    def _setup_llm(self) -> Optional[LLM]:
        raise NotImplementedError

    def _create_agents(self) -> Dict[str, Agent]:
        raise NotImplementedError

    def _create_tasks(self) -> List[Task]:
        if not self.agents:
            self._create_agents()

        tasks = [
            Task(
                description=f"Research deeply about: {self.topic}",
                expected_output="Detailed research findings in structured format",
                agent=self.agents["researcher"],
                tools=[self.search_manager.search]
            ),
            Task(
                description=f"Analyze findings about: {self.topic}",
                expected_output="Comprehensive analysis with key insights",
                agent=self.agents["analyzer"]
            )
        ]
        return tasks

    def run(self) -> Dict[str, Any]:
        try:
            agents = self._create_agents()
            tasks = self._create_tasks()

            crew = Crew(
                agents=list(agents.values()),
                tasks=tasks,
                verbose=True,
                process="sequential"
            )

            result = crew.kickoff()
            self._save_output(result)
            return result

        except Exception as e:
            error_result = {
                "error": str(e),
                "status": "failed",
                "timestamp": datetime.now().isoformat()
            }
            self._save_output(error_result)
            raise

    def _save_output(self, result: Dict[str, Any]) -> None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = self.output_dir / f"{self.__class__.__name__}_{timestamp}.json"
        with open(output_file, "w") as f:
            json.dump(result, f, indent=2)

    def _get_tools_for_agent(self, tool_names: List[str]):
        try:
            return self.tool_factory.get_tools_for_agent(tool_names)
        except Exception as e:
            logger.error(f"Failed to get tools: {str(e)}")
            return []

class GeminiCrew(BaseModelCrew):
    def __init__(self, *args, **kwargs):
        self.model_type = os.getenv("GEMINI_MODEL", "gemini-2.5-pro-exp-03-25")
        self.thinking_mode = os.getenv("GEMINI_THINKING_MODE", "enhanced")
        super().__init__(*args, **kwargs)

    def _setup_llm(self) -> LLM:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")

        # Configure model based on type
        if self.model_type == os.getenv("GEMINI_2_5_PRO"):
            max_tokens = int(os.getenv("GEMINI_2_5_MAX_TOKENS", "32768"))
            context_window = int(os.getenv("GEMINI_2_5_CONTEXT_WINDOW", "1000000"))
        elif "thinking" in self.model_type.lower():
            max_tokens = int(os.getenv("GEMINI_MAX_TOKENS", "8192"))
            context_window = int(os.getenv("GEMINI_CONTEXT_WINDOW", "1000000"))
        else:
            max_tokens = int(os.getenv("GEMINI_MAX_TOKENS", "8192"))
            context_window = int(os.getenv("GEMINI_CONTEXT_WINDOW", "1000000"))

        return LLM(
            model=f"gemini/{self.model_type}",
            api_key=api_key,
            temperature=float(os.getenv("GEMINI_TEMPERATURE", "0.7")),
            max_tokens=max_tokens,
            context_window=context_window,
            top_p=float(os.getenv("GEMINI_TOP_P", "0.95")),
            model_kwargs={
                "thinking_mode": self.thinking_mode,
                "features": os.getenv("GEMINI_2_5_FEATURES", "").split(",")
            }
        )

    def _create_agents(self) -> Dict[str, Agent]:
        try:
            # Set agent configurations based on model capabilities
            researcher_config = {
                "tools": ["web_search", "file_analyzer", "knowledge_base"]
            }
            analyzer_config = {
                "tools": ["structured_analysis", "validation_tool", "insight_generator"]
            }

            # Add enhanced capabilities for 2.5 Pro
            if self.model_type == os.getenv("GEMINI_2_5_PRO"):
                researcher_config["tools"].extend(["advanced_reasoning", "tool_use"])
                analyzer_config["tools"].extend(["multimodal_analysis", "code_generation"])

            self.agents = {
                "researcher": Agent(
                    role="Research Expert",
                    goal="Conduct comprehensive research with advanced reasoning",
                    backstory="Expert researcher with advanced analytical capabilities",
                    allow_delegation=True,
                    llm=self.llm,
                    tools=self._get_tools_for_agent(researcher_config["tools"]) + [self.search_manager.search],
                    verbose=True
                ),
                "analyzer": Agent(
                    role="Analysis Expert",
                    goal="Process and analyze findings with enhanced thinking",
                    backstory="Expert analyst with advanced pattern recognition",
                    allow_delegation=True,
                    llm=self.llm,
                    tools=self._get_tools_for_agent(analyzer_config["tools"]),
                    verbose=True
                )
            }
            return self.agents
        except Exception as e:
            logger.error(f"Failed to create Gemini agents: {str(e)}")
            raise

class LMStudioCrew(BaseModelCrew):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _setup_llm(self) -> LLM:
        api_base = os.getenv("LMSTUDIO_API_URL", "http://localhost:1234")
        model = os.getenv("LMSTUDIO_MODEL", "gemma-3-4b-it")

        try:
            return LLM(
                model=f"openai/{model}",  # LM Studio uses OpenAI-compatible endpoint
                base_url=f"{api_base}/v1",
                temperature=float(os.getenv("LMSTUDIO_TEMPERATURE", "0.7")),
                max_tokens=int(os.getenv("LMSTUDIO_MAX_TOKENS", "2048")),
                top_p=float(os.getenv("LMSTUDIO_TOP_P", "0.95"))
            )
        except Exception as e:
            logger.error(f"Failed to initialize LM Studio LLM: {str(e)}")
            raise

    def _create_agents(self) -> Dict[str, Agent]:
        try:
            self.agents = {
                "researcher": Agent(
                    role="Research Expert",
                    goal="Conduct thorough research on the given topic",
                    backstory="Expert at gathering and analyzing information from various sources",
                    allow_delegation=True,
                    llm=self.llm,
                    tools=self._get_tools_for_agent([
                        "web_search",
                        "file_analyzer",
                        "knowledge_base"
                    ]) + [self.search_manager.search],
                    verbose=True
                ),
                "analyzer": Agent(
                    role="Analysis Expert",
                    goal="Process and structure research findings",
                    backstory="Expert at breaking down complex topics and extracting key insights",
                    allow_delegation=True,
                    llm=self.llm,
                    tools=self._get_tools_for_agent([
                        "structured_analysis",
                        "validation_tool",
                        "insight_generator"
                    ]),
                    verbose=True
                )
            }
            return self.agents
        except Exception as e:
            logger.error(f"Failed to create LM Studio agents: {str(e)}")
            raise
