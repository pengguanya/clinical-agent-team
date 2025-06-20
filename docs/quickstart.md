# Quick Start Guide

This guide will help you get up and running with the Clinical Agent Teams project quickly.

## Prerequisites

- Python 3.9+ installed
- Git installed
- Access to API keys for:
  - OpenAI API or Groq API
  - Serper.dev API (for web search)
  - Supabase (optional, for data persistence)

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/clinical-agent-team.git
cd clinical-agent-team
```

2. **Create a virtual environment**

```bash
# For macOS/Linux
python -m venv .venv
source .venv/bin/activate

# For Windows
python -m venv .venv
.venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

```bash
cp .env.example .env
```

Edit the `.env` file with your API keys:

```
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

## Running Your First Agent Team

### Clinical Study Design Team

To run the Clinical Study Design Team example:

```bash
python src/agent_teams/clinical_study_design/clinical_study_multiagent.py
```

```bash
python src/crews/use_case_report_creation/use_case_multiagent.py
```

This will:
1. Initialize the crew with multiple AI agents
2. Execute a workflow to generate a report on a specified topic
3. Output a markdown article and social media posts

You can modify the input parameters in the script to change the topic:

```python
inputs = {
    "sector": "Public Sector",
    "topic": "AI for public service and citizen engagement",
    "examples": "AI for Public Service and Citizen Engagement: LLM-driven assistants that help citizens apply for permits, schedule appointments, and file complaints with minimal human intervention."
}
```

### Customizing Agents

You can customize the agents by editing the config files in the respective crew's config directory:

```yaml
# File: src/crews/use_case_report_creation/config/agents.yaml
market_intelligence_agent:
  role: "Market Intelligence Specialist"
  goal: "Conduct comprehensive market research and gather intelligence on the specified topic."
  backstory: "You are a seasoned market intelligence specialist with a keen eye for emerging trends..."
```

### Creating Your Own Crew

To create your own crew:

1. **Create a new directory** for your crew in `src/crews/your_crew_name/`
2. **Create a config directory** for agent and task configurations
3. **Create agent and task YAML files** defining your crew's components
4. **Create a main script** similar to the examples, defining agents, tasks, and the crew

## Troubleshooting

### API Rate Limits

If you encounter rate limit errors:
- Reduce the verbosity of the crew
- Add delays between agent operations
- Use a different LLM provider

### Memory Issues

If you encounter memory issues:
- Reduce the complexity of the crew
- Limit the number of concurrent agents
- Use a more efficient LLM model

## Next Steps

After getting familiar with the basic operation:

1. Explore the different crews in the repository
2. Try modifying existing crews to suit your needs
3. Create your own custom crews for specific use cases
4. Contribute to the project by adding new features or improving existing ones 