"""
Ollama project initialization.
"""
from .multi_gemini_crew import GeminiMultiCrew
from .tools.tool_factory import ToolFactory

__version__ = "2.0.0"
__all__ = ["GeminiMultiCrew", "ToolFactory"]
