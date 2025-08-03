# Warning control
import warnings

warnings.filterwarnings("ignore")

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

import os
import yaml
import textwrap
from crewai import Agent, Task, Crew
from pydantic import BaseModel, Field
from typing import List
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool
from IPython.display import display, Markdown


class SocialMediaPost(BaseModel):
    platform: str = Field(
        ...,
        description="The social media platform where the post will be published (e.g., Twitter, LinkedIn, Instagram).",
    )
    content: str = Field(
        ...,
        description="The content of the social media post, including any hashtags or mentions.",
    )


class ContentOutput(BaseModel):
    article: str = Field(..., description="The article, formatted in markdown.")
    social_media_posts: List[SocialMediaPost] = Field(
        ..., description="A list of social media posts related to the article."
    )


# Define file paths for YAML configurations
files = {"agents": "config/agents.yaml", "tasks": "config/tasks.yaml"}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, "r") as file:
        configs[config_type] = yaml.safe_load(file)

# Assign loaded configurations to specific variables
agents_config = configs["agents"]
tasks_config = configs["tasks"]

os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"
# os.environ["GROQ_API_KEY"] = "gsk_6666666666666666666666666666666666666666666666666666666666666666"
groq_llm = "groq/llama-3.1-70b-versatile"
# Creating Agents
market_intelligence_agent = Agent(
    config=agents_config["market_intelligence_agent"],
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    # llm=groq_llm,
)

data_analyst_agent = Agent(
    config=agents_config["data_analyst_agent"], 
    tools=[SerperDevTool(), WebsiteSearchTool()],
    # llm=groq_llm,
)

content_creator_agent = Agent(
    config=agents_config["content_creator_agent"],
    tools=[SerperDevTool(), WebsiteSearchTool()],
)

quality_assurance_agent = Agent(
    config=agents_config["quality_assurance_agent"],
)

# Creating Tasks
monitor_market_intelligence_task = Task(
    config=tasks_config["monitor_market_intelligence"],
    agent=market_intelligence_agent
)

analyze_market_data_task = Task(
    config=tasks_config["analyze_market_data"],
    agent=data_analyst_agent
)

create_content_task = Task(
    config=tasks_config["create_content"],
    agent=content_creator_agent,
