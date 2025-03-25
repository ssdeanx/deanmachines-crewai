from typing import Dict, List
import os
import yaml
from pathlib import Path
from .agent_tools import (
    WebSearchTool,
    FileAnalyzerTool,
    KnowledgeBaseTool,
    StructuredAnalysisTool,
    ValidationTool,
    InsightGeneratorTool
)
from .advanced_tools import (
    AdvancedReasoningTool,
    MultimodalAnalysisTool,
    ThinkingModeTool,
    ToolUseTool
)
from .generation_tools import (
    CodeGenerationTool,
    ImageGenerationTool,
    AudioGenerationTool
)

class ToolFactory:
    def __init__(self):
        self.config = self._load_config()
        self.tools = {}
        self.thinking_mode = os.getenv("GEMINI_THINKING_MODE", "enhanced")

    def _load_config(self) -> Dict:
        config_path = Path(__file__).parent.parent / "config" / "tools.yaml"
        with open(config_path) as f:
            return yaml.safe_load(f)

    def get_tool(self, tool_name: str):
        if tool_name in self.tools:
            return self.tools[tool_name]

        config = self.config.get(tool_name)
        if not config:
            raise ValueError(f"Tool not found: {tool_name}")

        tool = self._create_tool(tool_name, config)
        self.tools[tool_name] = tool
        return tool

    def _create_tool(self, name: str, config: Dict):
        # Basic tools
        if name == "web_search":
            return WebSearchTool(
                api_key=os.getenv("SERPER_API_KEY"),
                max_results=config["args"]["max_results"]
            )
        elif name == "file_analyzer":
            return FileAnalyzerTool(
                supported_formats=config["args"]["supported_formats"],
                max_file_size=config["args"]["max_file_size"]
            )
        elif name == "knowledge_base":
            return KnowledgeBaseTool(
                base_path=config["args"]["base_path"],
                index_type=config["args"]["index_type"]
            )
        elif name == "structured_analysis":
            return StructuredAnalysisTool(
                formats=config["args"]["formats"],
                validation=config["args"]["validation"]
            )
        elif name == "validation_tool":
            return ValidationTool(
                criteria=config["args"]["criteria"],
                threshold=config["args"]["threshold"]
            )
        elif name == "insight_generator":
            return InsightGeneratorTool(
                formats=config["args"]["formats"],
                max_insights=config["args"]["max_insights"],
                min_confidence=config["args"]["min_confidence"]
            )
        # Generation tools
        elif name == "code_generation":
            return CodeGenerationTool()
        elif name == "image_generation":
            return ImageGenerationTool()
        elif name == "audio_generation":
            return AudioGenerationTool()
        # Advanced Gemini 2.5 tools
        elif name == "advanced_reasoning":
            return AdvancedReasoningTool()
        elif name == "multimodal_analysis":
            return MultimodalAnalysisTool()
        elif name == "thinking_mode":
            return ThinkingModeTool(mode=self.thinking_mode)
        elif name == "tool_use":
            return ToolUseTool()
        raise ValueError(f"Unknown tool type: {name}")

    def get_tools_for_agent(self, tool_names: List[str]):
        return [self.get_tool(name) for name in tool_names]
