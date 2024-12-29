import os
from langchain.tools import tool

class FileTools:
    @tool("read_file")
    def read_file(self, file_path: str) -> str:
        """Reads a file's content."""
        if not os.path.exists(file_path):
            return f"File '{file_path}' not found."
        with open(file_path, 'r') as file:
            return file.read()

    @tool("write_file")
    def write_file(self, file_path: str, content: str) -> str:
        """Writes content to a file."""
        try:
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as file:
                file.write(content)
            return f"Written to '{file_path}'."
        except Exception as e:
            return f"Error: {e}"