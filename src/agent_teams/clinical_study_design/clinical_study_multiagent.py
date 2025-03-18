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

# Define Pydantic Models for Structured Output
class ProtocolSection(BaseModel):
    section_title: str = Field(..., description="Title of the protocol section (e.g., 'Study Objectives').")
    content: str = Field(..., description="Content of the section.")

class ClinicalProtocol(BaseModel):
    title: str = Field(..., description="Full title of the clinical study.")
    protocol_sections: List[ProtocolSection] = Field(..., description="List of protocol sections.")
    summary: str = Field(..., description="Executive summary of the protocol.")

# Define file paths for YAML configurations
# Using absolute paths based on the script location to ensure it runs from anywhere
base_dir = os.path.dirname(os.path.abspath(__file__))
files = {
    "agents": os.path.join(base_dir, "config/agents.yaml"),
    "tasks": os.path.join(base_dir, "config/tasks.yaml")
}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, "r", encoding="utf-8") as file:
        configs[config_type] = yaml.safe_load(file)

# Assign loaded configurations to specific variables
agents_config = configs["agents"]
tasks_config = configs["tasks"]

os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"

# Creating Agents
principal_investigator = Agent(
    config=agents_config["principal_investigator"],
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
)

biostatistician = Agent(
    config=agents_config["biostatistician"],
    tools=[SerperDevTool(), WebsiteSearchTool()],
)

clinical_data_manager = Agent(
    config=agents_config["clinical_data_manager"],
    tools=[SerperDevTool()],
)

