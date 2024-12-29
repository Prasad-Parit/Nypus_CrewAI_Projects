import requests
from langchain.tools import tool

class CustomTools:

    @tool("scrape_website")
    def scrape_website(self, url: str) -> str:
        """Scrape the content of a webpage."""
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text[:500]  # Trimmed for simplicity
            else:
                return f"Error: HTTP {response.status_code}"
        except Exception as e:
            return f"Error while scraping: {e}"
