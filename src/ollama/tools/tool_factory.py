"""
Simplified ToolFactory for test harnesses.
This provides basic tool creation functionality needed for multi-agent testing.
"""
import os
import logging
from typing import Optional, Any
from langchain.tools import Tool

class ToolFactory:
    """
    A simplified factory for creating tools used in test harnesses.
    Currently supports only the 'web_search' tool using SerperDev.
    """

    def __init__(self):
        """Initialize the ToolFactory with basic configuration."""
        self.logger = logging.getLogger(__name__)
        self.available_tools = {
            "web_search": self._create_web_search_tool
        }

    def get_tool(self, name: str) -> Optional[Any]:
        """
        Get a tool instance by name.

        Args:
            name: The name of the tool to retrieve

        Returns:
            The tool instance if available, otherwise raises KeyError

        Raises:
            KeyError: If the tool name is not recognized
            Exception: If tool creation fails due to missing dependencies or API keys
        """
        if name not in self.available_tools:
            raise KeyError(f"Tool '{name}' not found. Available tools: {list(self.available_tools.keys())}")

        return self.available_tools[name]()

    def _create_web_search_tool(self) -> Any:
        """
        Create a web search tool using the Serper API.

        Returns:
            A web search tool instance

        Raises:
            Exception: If SERPER_API_KEY is not set or other initialization fails
        """
        serper_api_key = os.getenv("SERPER_API_KEY")
        if not serper_api_key:
            raise ValueError("SERPER_API_KEY environment variable not set")

        try:
            from langchain.utilities import SerpAPIWrapper

            search = SerpAPIWrapper(serpapi_api_key=serper_api_key)

            return Tool(
                name="web_search",
                description="Search the web for information on a topic. Use this when you need current or factual information.",
                func=search.run
            )
        except ImportError as e:
            raise Exception(f"Failed to create web_search tool. Dependency error: {e}")
        except Exception as e:
            raise Exception(f"Failed to create web_search tool: {e}")
