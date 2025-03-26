"""
Read and write tool for agents to use for file operations.
Supports MLflow metrics tracking and enhanced error recovery.
"""
import os
import logging
from pathlib import Path
from langchain.tools import BaseTool
import mlflow

logger = logging.getLogger(__name__)

class ReadWriteTool(BaseTool):
    """
    Tool for reading from and writing to files in a workspace.
    Provides capabilities for agents to save and retrieve information with enhanced error recovery
    and performance monitoring via MLflow.
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

        # Track file operations for performance monitoring
        self.operation_counts = {
            "read": 0,
            "write": 0,
            "append": 0,
            "list": 0,
            "errors": 0
        }

        logger.info(f"ReadWriteTool initialized with workspace: {self.workspace_path}")

    def _run(self, command: str, filename: str = None, content: str = None) -> str:
        """
        Run the tool with the specified command, filename, and optional content.
        Now includes error recovery and MLflow metrics tracking.

        Args:
            command: The operation to perform ('read', 'write', 'append', 'list')
            filename: The name of the file to read from or write to
            content: The content to write (required for 'write' and 'append' commands)

        Returns:
            The result of the operation as a string
        """
        try:
            # Increment operation counter
            if command in self.operation_counts:
                self.operation_counts[command] += 1

            # Log operation metrics to MLflow if available
            try:
                mlflow.log_metrics({
                    f"file_ops_{command}": self.operation_counts[command],
                    "file_ops_total": sum(count for op, count in self.operation_counts.items() if op != "errors")
                })
            except Exception:
                # Silently continue if MLflow logging fails
                pass

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
            # Track error
            self.operation_counts["errors"] += 1

            # Log error metric to MLflow if available
            try:
                mlflow.log_metrics({"file_ops_errors": self.operation_counts["errors"]})
            except Exception:
                pass

            error_msg = f"Error executing {command} operation: {str(e)}"
            logger.error(error_msg)

            # Attempt error recovery
            if command in ["write", "append"]:
                try:
                    # Backup the content to a recovery file
                    recovery_path = os.path.join(self.workspace_path, f"recovery_{filename}")
                    with open(recovery_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    logger.info(f"Content backed up to recovery file: {recovery_path}")
                    return f"{error_msg}\nContent backed up to recovery file: {recovery_path}"
                except Exception as backup_error:
                    logger.error(f"Failed to create recovery file: {backup_error}")

            return error_msg

    def _read_file(self, file_path: str) -> str:
        """
        Read content from a file with enhanced error handling.

        Args:
            file_path: Path to the file to read

        Returns:
            The file contents as a string
        """
        if not os.path.exists(file_path):
            return f"Error: File '{os.path.basename(file_path)}' not found."

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Track file size for performance monitoring
            file_size = os.path.getsize(file_path)
            try:
                mlflow.log_metric(f"file_read_size_bytes", file_size)
            except Exception:
                pass

            logger.info(f"Successfully read file: {os.path.basename(file_path)} ({file_size} bytes)")
            return content
        except Exception as e:
            raise RuntimeError(f"Failed to read file: {str(e)}")

    def _write_file(self, file_path: str, content: str, mode: str = 'w') -> str:
        """
        Write or append content to a file with enhanced error handling.

        Args:
            file_path: Path to the file to write to
            content: Content to write
            mode: Write mode ('w' for write, 'a' for append)

        Returns:
            Success message string
        """
        try:
            # Create a temporary file first
            temp_path = f"{file_path}.tmp"
            with open(temp_path, mode, encoding='utf-8') as f:
                f.write(content)

            # If successful, rename to the actual file
            if os.path.exists(file_path):
                os.replace(temp_path, file_path)
            else:
                os.rename(temp_path, file_path)

            # Track file size for performance monitoring
            file_size = os.path.getsize(file_path)
            try:
                mlflow.log_metric(f"file_write_size_bytes", file_size)
            except Exception:
                pass

            operation = "appended to" if mode == 'a' else "written to"
            logger.info(f"Successfully {operation} file: {os.path.basename(file_path)} ({file_size} bytes)")
            return f"Successfully {operation} file: {os.path.basename(file_path)}"

        except Exception as e:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except Exception:
                    pass
            raise RuntimeError(f"Failed to write to file: {str(e)}")

    def _list_files(self) -> str:
        """
        List all files in the workspace with enhanced information.

        Returns:
            A string containing the list of files and their sizes
        """
        try:
            files = []
            total_size = 0

            for f in os.listdir(self.workspace_path):
                file_path = os.path.join(self.workspace_path, f)
                if os.path.isfile(file_path):
                    size = os.path.getsize(file_path)
                    total_size += size
                    size_str = self._format_size(size)
                    files.append(f"{f} ({size_str})")

            if not files:
                return "No files found in workspace."

            # Track total workspace size
            try:
                mlflow.log_metric("workspace_total_size_bytes", total_size)
            except Exception:
                pass

            files_list = "\n".join(files)
            total_size_str = self._format_size(total_size)
            return f"Files in workspace (Total: {total_size_str}):\n{files_list}"

        except Exception as e:
            raise RuntimeError(f"Failed to list files: {str(e)}")

    def _format_size(self, size: int) -> str:
        """Format file size in human-readable format."""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size < 1024:
                return f"{size:.1f}{unit}"
            size /= 1024
        return f"{size:.1f}TB"

    async def _arun(self, command: str, filename: str = None, content: str = None) -> str:
        """
        Async implementation of the tool.

        Args:
            command: The operation to perform
            filename: Optional filename
            content: Optional content

        Returns:
            The result of the operation
        """
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
