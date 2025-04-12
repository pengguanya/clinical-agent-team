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
