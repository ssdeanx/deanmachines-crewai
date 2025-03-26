"""
Simplified ToolFactory for test harnesses.
Provides basic tool creation functionality needed for multi-agent testing.
Includes web search, current datetime, and sandboxed file read/write within './knowledge'.
"""
import os
import logging
import datetime
import json
import aiohttp

from typing import Optional, Any, Dict
from langchain.tools import Tool
from langchain_community.utilities import GoogleSerperAPIWrapper as SerpAPIWrapper
from langchain_core.utils import get_from_dict_or_env

# --- Define a single safe base directory for file operations ---
SAFE_FILE_DIR = os.path.abspath("./knowledge")

# --- Helper Functions (Use revised versions from above) ---
# ... (paste the revised get_current_datetime_func, read_file_func, write_file_func here) ...

# --- Helper Functions ---

# Use *_args, **_kwargs to signal intention to ignore captured arguments
def get_current_datetime_func(*_args, **_kwargs) -> str:
    """Returns the current date and time as a formatted string. Ignores any input arguments."""
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# ... (read_file_func and write_file_func remain the same) ...
def read_file_func(filepath: str) -> str:
    """
    Reads the content of a specified file within the safe directory ('./knowledge').
    Args: filepath (relative path). Returns: File content or error message.
    """
    if not filepath or '..' in filepath or os.path.isabs(filepath):
        return "Error: Invalid or potentially unsafe filepath provided. Only relative paths within the allowed directory are permitted."
    try: os.makedirs(SAFE_FILE_DIR, exist_ok=True)
    except OSError as e: return f"Error: Could not ensure safe directory exists '{SAFE_FILE_DIR}'. {str(e)}"
    full_path = os.path.abspath(os.path.join(SAFE_FILE_DIR, filepath))
    if not full_path.startswith(SAFE_FILE_DIR):
        return f"Error: Access denied. Attempted to read outside the allowed directory: '{filepath}'"
    try:
        with open(full_path, 'r', encoding='utf-8') as f: content = f.read()
        return f"Successfully read content from '{filepath}' (in {SAFE_FILE_DIR}):\n---\n{content}\n---"
    except FileNotFoundError: return f"Error: File not found at '{filepath}' within the allowed directory ('{SAFE_FILE_DIR}')."
    except Exception as e: return f"Error reading file '{filepath}' from '{SAFE_FILE_DIR}': {str(e)}"

def write_file_func(input_json: str) -> str:
    """
    Writes content to a specified file within the safe directory ('./knowledge').
    Args: input_json (string): {'filepath': 'relative/path.txt', 'content': 'Text'}. Returns: Confirmation or error.
    """
    try:
        data = json.loads(input_json)
        filepath = data.get('filepath'); content = data.get('content')
        if not filepath or not isinstance(filepath, str) or '..' in filepath or os.path.isabs(filepath):
            return "Error: Invalid or potentially unsafe 'filepath' provided in JSON. Only relative paths are allowed."
        if content is None or not isinstance(content, str):
            return "Error: Invalid or missing 'content' (must be a string) provided in JSON."
        try: os.makedirs(SAFE_FILE_DIR, exist_ok=True)
        except OSError as e: return f"Error: Could not create safe directory '{SAFE_FILE_DIR}'. {str(e)}"
        full_path = os.path.abspath(os.path.join(SAFE_FILE_DIR, filepath))
        if not full_path.startswith(SAFE_FILE_DIR):
            return f"Error: Access denied. Attempted to write outside the allowed directory: '{filepath}'"
        try: os.makedirs(os.path.dirname(full_path), exist_ok=True)
        except OSError as e:
             if os.path.exists(os.path.dirname(full_path)) and not os.path.isdir(os.path.dirname(full_path)):
                 return f"Error: Cannot create subdirectory for '{filepath}'. A file exists with the same name as a required directory."
             return f"Error: Could not create subdirectories for '{filepath}' within '{SAFE_FILE_DIR}'. {str(e)}"
        with open(full_path, 'w', encoding='utf-8') as f: f.write(content)
        return f"Successfully wrote content to '{filepath}' within the allowed directory ('{SAFE_FILE_DIR}')."
    except json.JSONDecodeError: return "Error: Invalid JSON input. Expected format: {'filepath': 'path', 'content': 'text'}."
    except Exception as e:
        err_ctx = filepath if 'filepath' in locals() and filepath else input_json
        return f"Error writing file '{err_ctx}' to '{SAFE_FILE_DIR}': {str(e)}"


# --- ToolFactory Class ---
class ToolFactory:
    """
    A simplified factory for creating tools used in test harnesses.
    Supports 'web_search', 'datetime_tool', 'read_file', 'write_file'.
    File operations are restricted to the './knowledge' directory. # <-- Updated docstring
    """

    def __init__(self):
        """Initialize the ToolFactory with basic configuration."""
        self.logger = logging.getLogger(__name__)
        # Ensure the single safe directory exists on initialization
        try:
            os.makedirs(SAFE_FILE_DIR, exist_ok=True) # Use SAFE_FILE_DIR
            self.logger.info(f"Ensured safe file directory exists: {SAFE_FILE_DIR}")
        except OSError as e:
            self.logger.error(f"Could not create safe file directory on init: {SAFE_FILE_DIR}. File tools may fail. Error: {e}")

        self.available_tools: Dict[str, callable] = {
            "web_search": self._create_web_search_tool,
            "datetime_tool": self._create_datetime_tool,
            "read_file": self._create_read_file_tool,
            "write_file": self._create_write_file_tool
        }
        self.logger.debug(f"ToolFactory initialized with tools: {list(self.available_tools.keys())}")

    def get_tool(self, name: str) -> Optional[Tool]:
        # ... (no changes needed here) ...
        if name not in self.available_tools:
            self.logger.error(f"Attempted to get unknown tool: '{name}'")
            raise KeyError(f"Tool '{name}' not found. Available tools: {list(self.available_tools.keys())}")
        try:
            tool_instance = self.available_tools[name]()
            self.logger.info(f"Successfully retrieved/created tool: '{name}'")
            return tool_instance
        except Exception as e:
            self.logger.error(f"Failed to create tool '{name}': {e}", exc_info=True)
            raise

    # --- Tool Creation Methods ---

    def _create_web_search_tool(self) -> Tool:
        """Creates the Google Serper web search tool."""
        # Ensure SERPER_API_KEY is used, matching the service
        serper_api_key = get_from_dict_or_env(
            {}, "serper_api_key", "SERPER_API_KEY" # Use helper for flexibility
        )
        # serper_api_key = os.getenv("SERPER_API_KEY") # Or simpler direct access
        if not serper_api_key:
            self.logger.error("SERPER_API_KEY environment variable not set for web search tool.")
            raise ValueError("SERPER_API_KEY environment variable not set")
        try:
            self.logger.debug("Initializing GoogleSerperAPIWrapper...")
            # --- CORRECTED PARAMETER NAME ---
            search = SerpAPIWrapper(serper_api_key=serper_api_key)
            # --- End Correction ---
            self.logger.debug("GoogleSerperAPIWrapper initialized successfully.")
            return Tool(
                name="web_search",
                description="Search the web for information using Google Serper. Input should be a search query string.",
                func=search.run
            )
        except ImportError:
             # Should not happen if langchain_community installed, but good practice
             self.logger.error("Failed to import GoogleSerperAPIWrapper. Is langchain-community installed?")
             raise
        except Exception as e:
            self.logger.error(f"Exception creating web_search tool: {e}", exc_info=True)
            raise Exception(f"Failed to create web_search tool: {e}") from e


    def _create_datetime_tool(self) -> Tool:
        # ... (no changes needed here) ...
        self.logger.debug("Creating current date/time tool.")
        try:
            return Tool(
                name="get_current_datetime",
                description="Use this tool to get the current date and time. Any input provided to this tool is ignored.",
                func=get_current_datetime_func
            )
        except Exception as e:
            self.logger.error(f"Exception creating date/time tool: {e}", exc_info=True)
            raise Exception(f"Failed to create date/time tool: {e}") from e


    def _create_read_file_tool(self) -> Tool:
        """Creates the sandboxed file reading tool."""
        self.logger.debug("Creating file read tool.")
        try:
            # --- UPDATED DESCRIPTION ---
            desc = f"Reads content from a file within the '{SAFE_FILE_DIR}' directory. Input must be the relative filepath (e.g., 'notes.txt' or 'subdir/data.csv')."
            return Tool(
                name="read_file",
                description=desc,
                func=read_file_func
            )
        except Exception as e:
            self.logger.error(f"Exception creating file read tool: {e}", exc_info=True)
            raise Exception(f"Failed to create file read tool: {e}") from e

    def _create_write_file_tool(self) -> Tool:
        """Creates the sandboxed file writing tool."""
        self.logger.debug("Creating file write tool.")
        try:
            # --- UPDATED DESCRIPTION ---
            desc = (f"Writes or overwrites content to a file within the '{SAFE_FILE_DIR}' directory. "
                    "Input MUST be a JSON string with keys 'filepath' (relative path) and 'content' (string). "
                    "Example: { \"filepath\": \"analysis/result.txt\", \"content\": \"Final analysis result.\" }")
            return Tool(
                name="write_file",
                description=desc,
                func=write_file_func
            )
        except Exception as e:
            self.logger.error(f"Exception creating file write tool: {e}", exc_info=True)
            raise Exception(f"Failed to create file write tool: {e}") from e
