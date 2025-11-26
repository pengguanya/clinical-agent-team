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
    context=[monitor_market_intelligence_task, analyze_market_data_task],
)

quality_assurance_task = Task(
    config=tasks_config["quality_assurance"],
    agent=quality_assurance_agent,
    output_pydantic=ContentOutput,
)

# Creating Crew
content_report_creation_crew = Crew(
    agents=[
        market_intelligence_agent,
        data_analyst_agent,
        content_creator_agent,
        quality_assurance_agent,
    ],
    tasks=[
        monitor_market_intelligence_task,
        analyze_market_data_task,
        create_content_task,
        quality_assurance_task,
    ],
    verbose=True,
)

# inputs = {
#     "sector": "Public Sector",
#     "topic": "AI for public service and citizen engagement",
#     "examples": "AI for Public Service and Citizen Engagement: LLM-driven assistants that help citizens apply for permits, schedule appointments, and file complaints with minimal human intervention; Automated AI responses for common inquiries; NLP-based chatbots for citizen feedback analysis and service improvement.",
# }
# inputs = {
#     "sector": "Public Sector",
#     "topic": "AI for tourism and cultural heritage",
#     "examples": "AI for Tourism and Cultural Heritage: AI-based visitor flow optimization to reduce congestion in major tourist areas; Smart tourism assistants providing personalized recommendations and translations.",
# }
# inputs = {
#     "sector": "Public Sector",
#     "topic": "Smart Contract and Procurement Monitoring",
#     "examples": "Smart Contract and Procurement Monitoring: An agentic system that scrapes, processes, and recommends relevant public contracts based on specific criteria set by municipalities; Automatically highlights potential inefficiencies in resource allocation; Predictive analytics for contract renewal needs and budgeting.",
# }
inputs = {
    "sector": "Public Sector",
    "topic": "Budget Planning and Cost Control",
    "examples": "",
}

result = content_report_creation_crew.kickoff(inputs=inputs)

# Access social media posts directly
posts = result.social_media_posts
for post in posts:
    platform = post.platform
    content = post.content
    print(platform)
    wrapped_content = textwrap.fill(content, width=50)
    print(wrapped_content)
    print("-" * 50)

# Display article directly
display(Markdown(result.article))

# Save the article to a file
with open(f"{inputs['topic']}_article.md", "w") as file:
    file.write(result.article)

# Save the social media posts to a file
with open(f"{inputs['topic']}_social_media_posts.md", "w") as file:
    for post in posts:
        file.write(f"Platform: {post.platform}\n")
        file.write(f"Content: {post.content}\n")
        file.write("-" * 50 + "\n")


def format_markdown(content):
    # Add H1 title and proper spacing
    formatted_content = f"""# AI Applications in Budget Planning and Cost Control

## Professional Report: AI Applications in Budget Planning and Cost Control for the Public Sector

### Executive Summary

{content.replace('#### Executive Summary\n', '').strip()}"""

    # Save the formatted content
    with open("budget_planning_report.md", "w", encoding="utf-8") as f:
        f.write(formatted_content)

# Use the formatting function
format_markdown(result.article)
