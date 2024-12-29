import requests
import re
from langchain.tools import tool

class WebsiteSearchTool:
    @tool("search_website")
    def search_website(self, url: str, keyword: str) -> str:
        """Search a website for a specific keyword."""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                content = response.text
                if re.search(rf'\b{keyword}\b', content, re.IGNORECASE):
                    return f"Keyword '{keyword}' found in {url}."
                return f"Keyword '{keyword}' not found in {url}."
            else:
                return f"Error: HTTP {response.status_code}"
        except Exception as e:
            return f"Error: {e}"