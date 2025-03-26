"""
Read and write tool for agents to use for file operations.
"""
import os
import json
import logging
from pathlib import Path
from typing import Optional, Dict, Any, List
from langchain.tools import BaseTool

logger = logging.getLogger(__name__)

class ReadWriteTool(BaseTool):
    """
    Tool for reading from and writing to files in a workspace.
    Provides capabilities for agents to save and retrieve information.
    """

    name = "read_write_tool"
    description = "Read from or write to files in the workspace. Use for saving research, summaries, or reports."

    def __init__(self, workspace_path: str = None):
        """
        Initialize the ReadWriteTool with a specific workspace path.

        Args:
            workspace_path: Path to the workspace directory. If None, a default location is used.
        """
        super().__init__()

        if workspace_path is None:
            # Use a default path in the project
            project_root = Path(__file__).parent.parent.parent.parent
            workspace_path = os.path.join(project_root, "workspace")

        self.workspace_path = workspace_path
        os.makedirs(self.workspace_path, exist_ok=True)
        logger.info(f"ReadWriteTool initialized with workspace: {self.workspace_path}")

    def _run(self, command: str, filename: str = None, content: str = None) -> str:
        """
        Run the tool with the specified command, filename, and optional content.

        Args:
            command: The operation to perform ('read', 'write', 'append', 'list')
            filename: The name of the file to read from or write to
            content: The content to write (required for 'write' and 'append' commands)

        Returns:
            The result of the operation as a string
        """
        try:
            if command == "list":
                return self._list_files()

            if not filename:
                return "Error: Filename is required for read, write, and append operations."

            # Sanitize the filename to prevent path traversal
            filename = os.path.basename(filename)
            file_path = os.path.join(self.workspace_path, filename)

            if command == "read":
                return self._read_file(file_path)
            elif command == "write":
                if not content:
                    return "Error: Content is required for write operation."
                return self._write_file(file_path, content, mode='w')
            elif command == "append":
                if not content:
                    return "Error: Content is required for append operation."
                return self._write_file(file_path, content, mode='a')
            else:
                return f"Error: Unknown command '{command}'. Use 'read', 'write', 'append', or 'list'."
        except Exception as e:
            error_msg = f"Error executing {command} operation: {str(e)}"
            logger.error(error_msg)
            return error_msg

    def _read_file(self, file_path: str) -> str:
        """Read content from a file."""
        if not os.path.exists(file_path):
            return f"Error: File '{os.path.basename(file_path)}' not found."

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            logger.info(f"Successfully read file: {os.path.basename(file_path)}")
            return content
        except Exception as e:
            raise RuntimeError(f"Failed to read file: {str(e)}")

    def _write_file(self, file_path: str, content: str, mode: str = 'w') -> str:
        """Write or append content to a file."""
        try:
            with open(file_path, mode, encoding='utf-8') as f:
                f.write(content)

            operation = "appended to" if mode == 'a' else "written to"
            logger.info(f"Successfully {operation} file: {os.path.basename(file_path)}")
            return f"Successfully {operation} file: {os.path.basename(file_path)}"
        except Exception as e:
            raise RuntimeError(f"Failed to write to file: {str(e)}")

    def _list_files(self) -> str:
        """List all files in the workspace."""
        try:
            files = [f for f in os.listdir(self.workspace_path)
                    if os.path.isfile(os.path.join(self.workspace_path, f))]

            if not files:
                return "No files found in workspace."

            files_list = "\n".join(files)
            return f"Files in workspace:\n{files_list}"
        except Exception as e:
            raise RuntimeError(f"Failed to list files: {str(e)}")

    def _arun(self, command: str, filename: str = None, content: str = None) -> str:
        """Async implementation of the tool."""
        # For now, just call the sync version
        return self._run(command, filename, content)


def get_read_write_tool(workspace_path: str = None) -> ReadWriteTool:
    """
    Factory function to create a ReadWriteTool instance.

    Args:
        workspace_path: Path to the workspace directory. If None, a default is used.

    Returns:
        An initialized ReadWriteTool instance
    """
    return ReadWriteTool(workspace_path=workspace_path)
