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

medical_writer = Agent(
    config=agents_config["medical_writer"],
)

# Creating Tasks
define_objectives_task = Task(
    config=tasks_config["define_study_objectives"],
    agent=principal_investigator
)

design_stats_task = Task(
    config=tasks_config["design_statistical_plan"],
    agent=biostatistician
)

plan_dm_task = Task(
    config=tasks_config["plan_data_management"],
    agent=clinical_data_manager
)

draft_protocol_task = Task(
    config=tasks_config["draft_protocol"],
    agent=medical_writer,
    context=[define_objectives_task, design_stats_task, plan_dm_task],
    output_pydantic=ClinicalProtocol,
)

# Creating Clinical Study Team
clinical_study_team = Crew(
    agents=[
        principal_investigator,
        biostatistician,
        clinical_data_manager,
        medical_writer,
    ],
    tasks=[
        define_objectives_task,
        design_stats_task,
        plan_dm_task,
        draft_protocol_task,
    ],
    verbose=True,
)

# Example Execution
print("Starting Clinical Study Design Team...")
result = clinical_study_team.kickoff(
    inputs={"medical_condition": "Type 2 Diabetes Mellitus with early-stage kidney disease"}
)

# Display Results
print("\n\n########################")
print("## CLINICAL PROTOCOL ##")
print("########################\n")
print(f"Title: {result.title}\n")
print(f"Summary: {result.summary}\n")
print("Sections:")
for section in result.protocol_sections:
    print(f"--- {section.section_title} ---")
    print(textwrap.fill(section.content, width=80))
    print("\n")

