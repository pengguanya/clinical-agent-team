# Clinical Agent Teams - AI Multi-Agent System

## Project Overview
This repository contains a specialized multi-agent AI system designed for **Clinical Study Design, Clinical Data Management, and Statistical Analysis**. It utilizes coordinated teams of AI agents to automate and enhance complex workflows in the clinical research domain.

## Key Features
- **Clinical Agent Teams**: Specialized AI agents (e.g., Principal Investigator, Biostatistician, Medical Writer) working in coordinated workflows.
- **Clinical Study Design**: Automated generation of clinical study protocols, including statistical plans and data management strategies.
- **Task Automation**: Streamlines the process of defining study objectives, calculating sample sizes, and drafting regulatory documents.

## Technology Stack
- Python
- CrewAI and LangGraph for agent orchestration
- Various LLM models through OpenAI/Groq
- Web scraping and search tools for medical research
- Supabase for data persistence

## Project Structure
```
├── data              <- Data storage for models and processing
├── models            <- Trained models and configurations
├── notebooks         <- Jupyter notebooks for experimentation
├── reports           <- Generated analysis and reports
├── src               <- Source code for the project
    ├── agents        <- Individual agent definitions
    ├── agent_teams   <- Agent Team definitions and configurations
    │   ├── clinical_study_design  <- Clinical Study Design Team
    │   ├── sales                  <- (Legacy) Sales Support Team
    │   └── use_case_report_creation <- (Legacy) Report Creation Team
    ├── services      <- Service connections (Supabase, etc.)
    └── ui.py         <- User interface components
```

## Running the Project
1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - MacOS/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy `.env.example` to `.env` and fill in your API keys
6. Run the Clinical Study Design example: 
   `python src/agent_teams/clinical_study_design/clinical_study_multiagent.py`

## Examples
The repository contains examples of AI Agent Teams:
- **Clinical Study Design**: A team comprising a PI, Biostatistician, Data Manager, and Medical Writer that collaborates to produce a comprehensive Clinical Study Protocol.
- **Research Assistant**: Conducts in-depth research on specified topics
- **Content Creation**: Generates articles and social media content
