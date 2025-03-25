import os
from langchain.agents import AgentType, initialize_agent
from langchain.chains import LLMChain, AnalyzeDocumentChain
from langchain.prompts import PromptTemplate
from langchain.schema import BaseOutputParser
from langchain.output_parsers import XMLOutputParser
from langchain.memory import ConversationBufferMemory
from typing import Any, Dict, List, Optional, Union
import xml.etree.ElementTree as ET
from datetime import datetime
import logging
import mlflow
import time

logger = logging.getLogger(__name__)

class XMLThinkingOutputParser(BaseOutputParser):
    """Parser for XML-structured thinking patterns"""

    def parse(self, text: str) -> Dict:
        try:
            # Clean and normalize XML
            text = text.replace("```xml", "").replace("```", "").strip()
            root = ET.fromstring(text)

            return {
                "structure": self._parse_section(root),
                "metadata": {
                    "timestamp": datetime.now().isoformat(),
                    "version": "1.0"
                }
            }
        except ET.ParseError as e:
            logger.error(f"XML parsing error: {str(e)}")
            return {"error": str(e)}

    def _parse_section(self, element: ET.Element) -> Dict:
        """Parse XML section recursively"""
        result = {}

        # Handle CDATA sections
        if element.text and "![CDATA[" in element.text:
            result["content"] = element.text.split("![CDATA[")[1].split("]]")[0].strip()
        else:
            result["content"] = element.text.strip() if element.text else ""

        # Parse children
        for child in element:
            if child.tag not in result:
                result[child.tag] = self._parse_section(child)

        return result

class StructuredThinkingChain(LLMChain):
    """Chain for structured thinking using XML patterns"""

    def __init__(
        self,
        llm,
        template_path: str,
        memory: Optional[ConversationBufferMemory] = None,
        verbose: bool = False
    ):
        self.template_path = template_path
        with open(template_path, 'r') as f:
            template_content = f.read()

        prompt = PromptTemplate(
            template=template_content,
            input_variables=["context", "objective", "constraints"],
            output_parser=XMLThinkingOutputParser()
        )

        super().__init__(
            llm=llm,
            prompt=prompt,
            memory=memory,
            verbose=verbose
        )

class BranchAnalysisChain(LLMChain):
    """Chain for branching analysis patterns"""

    def __init__(
        self,
        llm,
        branch_depth: int = 3,
        branch_width: int = 3,
        memory: Optional[ConversationBufferMemory] = None,
        verbose: bool = False
    ):
        self.branch_depth = branch_depth
        self.branch_width = branch_width

        template = """
        <branch_analysis>
        <context>
        {context}
        </context>
        <parameters>
        - Depth: {branch_depth}
        - Width: {branch_width}
        - Constraints: {constraints}
        </parameters>
        Generate a comprehensive branch analysis with the specified depth and width.
        </branch_analysis>
        """

        prompt = PromptTemplate(
            template=template,
            input_variables=["context", "branch_depth", "branch_width", "constraints"],
            output_parser=XMLThinkingOutputParser()
        )

        super().__init__(
            llm=llm,
            prompt=prompt,
            memory=memory,
            verbose=verbose
        )

class ResearchAnalysisChain(AnalyzeDocumentChain):
    """Chain for research analysis with XML structure"""

    def __init__(
        self,
        llm,
        research_depth: str = "detailed",
        source_types: List[str] = None,
        verbose: bool = False
    ):
        self.research_depth = research_depth
        self.source_types = source_types or ["academic", "industry", "case-studies"]

        template = """
        <research_analysis>
        <parameters>
        - Depth: {research_depth}
        - Sources: {source_types}
        - Focus: {focus_areas}
        </parameters>
        <content>
        {document}
        </content>
        Analyze the document following the specified parameters.
        </research_analysis>
        """

        prompt = PromptTemplate(
            template=template,
            input_variables=["document", "research_depth", "source_types", "focus_areas"],
            output_parser=XMLThinkingOutputParser()
        )

        super().__init__(
            llm=llm,
            prompt=prompt,
            verbose=verbose
        )

class CodeExecutionChain(LLMChain):
    """Chain for code execution and analysis"""

    def __init__(
        self,
        llm,
        code_executor,
        vision_analyzer,
        memory: Optional[ConversationBufferMemory] = None,
        verbose: bool = False
    ):
        self.code_executor = code_executor
        self.vision_analyzer = vision_analyzer

        template = """
        <code_execution>
        <parameters>
        <![CDATA[
        Code: {code}
        Context: {context}
        Vision Analysis: {vision_context}
        ]]>
        </parameters>
        Execute and analyze the code with given context.
        </code_execution>
        """

        prompt = PromptTemplate(
            template=template,
            input_variables=["code", "context", "vision_context"],
            output_parser=XMLOutputParser()
        )

        super().__init__(
            llm=llm,
            prompt=prompt,
            memory=memory,
            verbose=verbose
        )

    def execute_with_vision(self, code: str, image_path: Optional[str] = None) -> Dict[str, Any]:
        """Execute code with optional vision analysis"""
        with mlflow.start_run(nested=True):
            start_time = time.time()
            try:
                # Log parameters
                mlflow.log_params({
                    "code_length": len(code),
                    "has_vision_input": bool(image_path)
                })

                vision_context = {}
                if image_path:
                    vision_context = self.vision_analyzer.analyze_code_image(image_path)
                    mlflow.log_metric("vision_analysis_success", 1 if vision_context.get("status") == "success" else 0)

                result = self.code_executor.execute_code(
                    code=code,
                    context={"vision_analysis": vision_context}
                )

                # Log execution metrics
                execution_time = time.time() - start_time
                mlflow.log_metrics({
                    "execution_time": execution_time,
                    "execution_success": 1 if result.get("status") == "success" else 0
                })

                return result

            except Exception as e:
                mlflow.log_metrics({
                    "execution_success": 0,
                    "error_count": 1
                })
                logger.error(f"Code execution failed: {str(e)}")
                return {
                    "error": str(e),
                    "status": "failed"
                }

class ModelManager:
    """Manages model initialization and configuration"""
    def __init__(self, model_config: Dict):
        self.config = model_config
        self.models = {}

    def get_model(self, model_type: str) -> Any:
        if model_type not in self.models:
            model_config = self.config["available_models"].get(model_type)
            if not model_config:
                raise ValueError(f"Unknown model type: {model_type}")

            if "gemini" in model_type:
                self.models[model_type] = self._init_gemini_model(model_config)
            elif "lmstudio" in model_type:
                self.models[model_type] = self._init_lmstudio_model(model_config)

        return self.models[model_type]

    def _init_gemini_model(self, config: Dict) -> Any:
        import google.generativeai as genai
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        return genai.GenerativeModel(
            model_name=config["name"],
            generation_config={
                "max_output_tokens": config["max_tokens"],
                "temperature": self.config["llm_settings"]["temperature"],
                "top_p": self.config["llm_settings"]["top_p"]
            }
        )

    def _init_lmstudio_model(self, config: Dict) -> Any:
        return {
            "model": config["name"],
            "base_url": os.getenv("LMSTUDIO_API_URL"),
            "context_size": config["context_window"],
            "max_tokens": config["max_tokens"]
        }

class AgentFactory:
    """Creates agents with appropriate model configurations"""
    def __init__(self, base_config: Dict):
        self.config = base_config
        self.model_manager = ModelManager(base_config)

    def create_agent(self, agent_config: Dict) -> Agent:
        model_type = agent_config["model"]["type"]
        model = self.model_manager.get_model(model_type)

        if isinstance(model, dict) and "base_url" in model:
            # LMStudio model configuration
            llm = LLM(
                model=model["model"],
                base_url=model["base_url"],
                max_tokens=model["max_tokens"]
            )
        else:
            # Gemini model configuration
            llm = LLM(model=model)

        return Agent(
            role=agent_config["role"],
            goal=agent_config["goal"],
            backstory=agent_config["backstory"],
            allow_delegation=agent_config.get("allow_delegation", True),
            llm=llm,
            tools=agent_config.get("tools", []),
            verbose=agent_config.get("verbose", True)
        )

# Update the create_structured_thinking_agent function
def create_structured_thinking_agent(
    llm,
    tools: List[Dict],
    template_path: str,
    agent_config: Dict,
    memory: Optional[ConversationBufferMemory] = None,
    verbose: bool = False
) -> AgentType:
    """Create an agent specialized in structured thinking with specific model configuration"""
    # Initialize factory with base config
    factory = AgentFactory(agent_config.get("base_config", {}))

    # Create agent with specified model
    agent = factory.create_agent(agent_config)

    # Add tools and memory
    agent.tools.extend(tools)
    if memory:
        agent.memory = memory

    return agent

# Update create_analysis_pipeline function to use model-specific configurations
def create_analysis_pipeline(
    base_config: Dict,
    template_path: str,
    research_depth: str = "detailed",
    branch_depth: int = 3,
    code_tools: Optional[Dict] = None,
    memory: Optional[ConversationBufferMemory] = None,
    verbose: bool = False
) -> Dict[str, Union[LLMChain, AgentType]]:
    """Create a complete analysis pipeline with model-specific configurations"""

    factory = AgentFactory(base_config)

    # Create chains with appropriate models
    structured_chain = StructuredThinkingChain(
        llm=factory.model_manager.get_model("gemini_flash"),
        template_path=template_path,
        memory=memory,
        verbose=verbose
    )

    branch_chain = BranchAnalysisChain(
        llm=factory.model_manager.get_model("gemini_flash_lite"),
        branch_depth=branch_depth,
        memory=memory,
        verbose=verbose
    )

    research_chain = ResearchAnalysisChain(
        llm=factory.model_manager.get_model("gemini_flash"),
        research_depth=research_depth,
        verbose=verbose
    )

    if code_tools:
        code_chain = CodeExecutionChain(
            llm=factory.model_manager.get_model("lmstudio"),
            code_executor=code_tools.get("executor"),
            vision_analyzer=code_tools.get("vision"),
            memory=memory,
            verbose=verbose
        )

        return {
            "structured": structured_chain,
            "branch": branch_chain,
            "research": research_chain,
            "code": code_chain,
            "agent": factory.create_agent(base_config.get("code_expert", {}))
        }

    return {
        "structured": structured_chain,
        "branch": branch_chain,
        "research": research_chain,
        "agent": factory.create_agent(base_config.get("researcher", {}))
    }
