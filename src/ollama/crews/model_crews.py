"""
Model-specific crew implementations with standardized base class.
Supports both Gemini and LM Studio model variants.
"""
from typing import Dict, Any, List, Optional
from crewai import Agent, Task, Crew
from langchain_core.language_models import LLM
import os
from pathlib import Path
from datetime import datetime
import json
from ..tools.search_tools import SerperSearchTool
import logging
from ..tools.tool_factory import ToolFactory

# Configure logging
logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)

class BaseModelCrew:
    """Base class for model-specific crews."""

    def __init__(self, topic: str = "AI and machine learning"):
        """Initialize base crew with common setup."""
        self.topic = topic
        self.agents: Dict[str, Agent] = {}
        self.output_dir = Path("outputs")
        self.output_dir.mkdir(exist_ok=True)
        self.tool_factory = ToolFactory()
        self.llm = self._setup_llm()
        self.search_tool = SerperSearchTool()

    def _setup_llm(self) -> Optional[LLM]:
        """Set up model-specific LLM."""
        raise NotImplementedError

    def _create_agents(self) -> Dict[str, Agent]:
        """Create model-specific agents."""
        raise NotImplementedError

    def _create_tasks(self) -> List[Task]:
        """Create sequential tasks for the agents."""
        if not self.agents:
            self._create_agents()

        tasks = [
            Task(
                description=f"Research deeply about: {self.topic}",
                expected_output="Detailed research findings in structured format",
                agent=self.agents["researcher"],
                tools=[self.search_tool.search]
            ),
            Task(
                description=f"Analyze findings about: {self.topic}",
                expected_output="Comprehensive analysis with key insights",
                agent=self.agents["analyzer"]
            )
        ]
        return tasks

    def run(self) -> Dict[str, Any]:
        """Execute the crew's tasks and save results."""
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
        """Save crew execution results to file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_file = self.output_dir / f"{self.__class__.__name__}_{timestamp}.json"
        with open(output_file, "w", encoding='utf-8') as f:
            json.dump(result, f, indent=2)

    def _get_tools(self, tool_names: List[str]) -> List[Any]:
        """Get tools by name from the tool factory."""
        tools = []
        for name in tool_names:
            try:
                if tool := self.tool_factory.get_tool(name):
                    tools.append(tool)
            except Exception as e:
                logger.warning(f"Failed to get tool {name}: {str(e)}")
        return tools

class GeminiCrew(BaseModelCrew):
    """Gemini-specific crew implementation."""

    def __init__(self, *args, **kwargs):
        """Initialize Gemini crew with model configuration."""
        self.model_type = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")
        self.thinking_mode = os.getenv("GEMINI_THINKING_MODE", "enhanced")
        super().__init__(*args, **kwargs)

    def _setup_llm(self) -> LLM:
        """Set up Gemini LLM with environment configuration."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")

        return LLM(
            model=self.model_type,
            api_key=api_key,
            temperature=float(os.getenv("GEMINI_TEMPERATURE", "0.7")),
            max_tokens=int(os.getenv("GEMINI_MAX_TOKENS", "8192")),
            context_window=int(os.getenv("GEMINI_CONTEXT_WINDOW", "1000000")),
            top_p=float(os.getenv("GEMINI_TOP_P", "0.95"))
        )

    def _create_agents(self) -> Dict[str, Agent]:
        """Create Gemini-specific agents with appropriate tools."""
        try:
            researcher_tools = self._get_tools(["web_search"]) + [self.search_tool.search]
            analyzer_tools = self._get_tools(["structured_analysis"])

            self.agents = {
                "researcher": Agent(
                    role="Research Expert",
                    goal="Conduct comprehensive research with advanced reasoning",
                    backstory="Expert researcher with advanced analytical capabilities",
                    allow_delegation=False,
                    llm=self.llm,
                    tools=researcher_tools,
                    verbose=True
                ),
                "analyzer": Agent(
                    role="Analysis Expert",
                    goal="Process and analyze findings with enhanced thinking",
                    backstory="Expert analyst with advanced pattern recognition",
                    allow_delegation=False,
                    llm=self.llm,
                    tools=analyzer_tools,
                    verbose=True
                )
            }
            return self.agents
        except Exception as e:
            logger.error(f"Failed to create Gemini agents: {str(e)}")
            raise

class LMStudioCrew(BaseModelCrew):
    """LM Studio-specific crew implementation."""

    def _setup_llm(self) -> LLM:
        """Set up LM Studio LLM with environment configuration."""
        api_base = os.getenv("LMSTUDIO_API_URL", "http://localhost:1234")
        model = os.getenv("LMSTUDIO_MODEL", "gemma-7b-it")

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
        """Create LM Studio-specific agents with appropriate tools."""
        try:
            researcher_tools = self._get_tools(["web_search"]) + [self.search_tool.search]
            analyzer_tools = self._get_tools(["structured_analysis"])

            self.agents = {
                "researcher": Agent(
                    role="Research Expert",
                    goal="Conduct thorough research on the given topic",
                    backstory="Expert at gathering and analyzing information from various sources",
                    allow_delegation=False,
                    llm=self.llm,
                    tools=researcher_tools,
                    verbose=True
                ),
                "analyzer": Agent(
                    role="Analysis Expert",
                    goal="Process and structure research findings",
                    backstory="Expert at breaking down complex topics and extracting key insights",
                    allow_delegation=False,
                    llm=self.llm,
                    tools=analyzer_tools,
                    verbose=True
                )
            }
            return self.agents
        except Exception as e:
            logger.error(f"Failed to create LM Studio agents: {str(e)}")
            raise
