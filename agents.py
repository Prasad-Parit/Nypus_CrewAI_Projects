from crewai import Agent
from textwrap import dedent
from langchain.chat_models import ChatOpenAI
from tools.custom_tools import CustomTools
from tools.file_tools import FileTools
from tools.search_tools import SearchTools
from tools.website_search_tool import WebsiteSearchTool


# Custom agents for the content creation project
class Content_Creation_Agents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4", temperature=0.7)
        

        # Initialize tool classes
        self.custom_tools = CustomTools()
        self.file_tools = FileTools()
        self.search_tools = SearchTools()
        self.website_search_tool = WebsiteSearchTool()

    def trend_researcher(self):
        return Agent(
            role="Trend Researcher",
            backstory=dedent(f"""A data-driven analyst with a knack for identifying emerging trends and audience interests."""),
            goal=dedent(f"""Generate blog post ideas based on trending topics."""),
            tools=[
                self.search_tools.search_internet,
                self.website_search_tool.search_website,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def seo_content_writer(self):
        return Agent(
            role="SEO Content Writer",
            backstory=dedent(f"""An experienced writer with expertise in SEO strategies, ensuring high visibility for online content."""),
            goal=dedent(f"""Write SEO-optimized articles and web content."""),
            tools=[
                self.file_tools.read_file,
                self.website_search_tool.search_website,
                self.search_tools.search_internet,
                self.file_tools.write_file,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def social_media_specialist(self):
        return Agent(
            role="Social Media Specialist",
            backstory=dedent(f"""A creative marketer skilled in crafting platform-specific content that engages diverse audiences."""),
            goal=dedent(f"""Create social media posts tailored to different platforms."""),
            tools=[
                self.file_tools.read_file,
                self.website_search_tool.search_website,
                self.search_tools.search_internet,
                self.file_tools.write_file,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def email_marketing_specialist(self):
        return Agent(
            role="Email Marketing Specialist",
            backstory=dedent(f"""A communications expert with a focus on persuasive writing and audience engagement through email campaigns."""),
            goal=dedent(f"""Develop email marketing content and newsletters."""),
            tools=[
                self.search_tools.search_internet,
                self.file_tools.write_file,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def ecommerce_copywriter(self):
        return Agent(
            role="E-commerce Copywriter",
            backstory=dedent(f"""A persuasive writer experienced in creating compelling product narratives that drive sales online."""),
            goal=dedent(f"""Craft product descriptions for e-commerce sites."""),
            tools=[
                self.website_search_tool.search_website,
                self.search_tools.search_internet,
                self.file_tools.write_file,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def video_scriptwriter(self):
        return Agent(
            role="Video Scriptwriter",
            backstory=dedent(f"""A skilled storyteller adept at transforming ideas into engaging scripts that resonate with viewers."""),
            goal=dedent(f"""Produce video scripts for promotional materials."""),
            tools=[
                self.website_search_tool.search_website,
                self.search_tools.search_internet,
                self.file_tools.write_file,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def infographic_designer(self):
        return Agent(
            role="Infographic Designer",
            backstory=dedent(f"""A creative designer with expertise in visual storytelling and data representation to simplify complex information."""),
            goal=dedent(f"""Design infographics based on data visualization principles."""),
            tools=[
                self.file_tools.read_file,
                self.file_tools.write_file,
            ],
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def content_coordinator(self):
        return Agent(
            role="Content Coordinator",
            backstory=dedent(f"""An organized leader with experience in reviewing and coordinating content to ensure alignment with overall strategies."""),
            goal=dedent(f"""Review all content outputs to ensure they align with the overarching strategy and are ready for deployment."""),
            tools=[
                self.file_tools.read_file,
                self.file_tools.write_file,
            ],
            allow_delegation=True,
            verbose=True,
            llm=self.OpenAIGPT4,
        )
