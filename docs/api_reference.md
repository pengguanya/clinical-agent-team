# API Reference

This document provides a reference for the main classes and functions in the Workforce Crews project.

## Core Components

### Agent

Agents are the building blocks of the system, representing specialized AI entities with specific roles and capabilities.

```python
from crewai import Agent

agent = Agent(
    role="Market Intelligence Specialist",
    goal="Conduct comprehensive market research and gather intelligence on the specified topic.",
    backstory="You are a seasoned market intelligence specialist with a keen eye for emerging trends...",
    tools=[SerperDevTool(), ScrapeWebsiteTool()],
    verbose=True,
    allow_delegation=False,
)
```

#### Parameters

- `role` (str): The agent's role or title
- `goal` (str): The agent's primary objective
- `backstory` (str): Contextual information about the agent
- `tools` (list): List of tools available to the agent
- `verbose` (bool): Whether to print detailed logs
- `allow_delegation` (bool): Whether the agent can delegate tasks to other agents

#### Methods

- `run(input_text)`: Execute the agent with the given input
- `get_tools()`: Return the tools available to the agent
- `get_memory()`: Return the agent's memory

### Task

Tasks are units of work assigned to agents.

```python
from crewai import Task

task = Task(
    description="Monitor market intelligence for the specified sector and topic.",
    expected_output="Comprehensive market intelligence report on the specified topic.",
    agent=market_intelligence_agent,
    context=[previous_task],
    output_pydantic=OutputSchema,
)
```

#### Parameters

- `description` (str): Description of the task
- `expected_output` (str): Description of the expected output
- `agent` (Agent): The agent assigned to the task
- `context` (list): List of tasks that provide context to this task
- `output_pydantic` (BaseModel): Pydantic model defining the output structure

#### Methods

- `execute(inputs)`: Execute the task with the given inputs
- `get_agent()`: Return the agent assigned to the task
- `get_context()`: Return the task's context

### Crew

Crews orchestrate multiple agents working on related tasks.

```python
from crewai import Crew

crew = Crew(
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
```

#### Parameters

- `agents` (list): List of agents in the crew
- `tasks` (list): List of tasks for the crew to execute
- `verbose` (bool): Whether to print detailed logs

#### Methods

- `kickoff(inputs)`: Start the crew's execution with the given inputs
- `get_agents()`: Return the agents in the crew
- `get_tasks()`: Return the tasks in the crew

## Tools

### SerperDevTool

Tool for performing web searches using the Serper.dev API.

```python
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()
```

#### Methods

- `search(query)`: Perform a web search with the given query

### ScrapeWebsiteTool

Tool for scraping content from websites.

```python
from crewai_tools import ScrapeWebsiteTool

scrape_tool = ScrapeWebsiteTool()
```

#### Methods

- `scrape(url)`: Scrape content from the given URL

### WebsiteSearchTool

Tool for searching within specific websites.

```python
from crewai_tools import WebsiteSearchTool

website_search_tool = WebsiteSearchTool()
```

#### Methods

- `search(query, website)`: Search for the query within the specified website

## Utility Functions

### load_yaml_config

Load configuration from YAML files.

```python
def load_yaml_config(file_path):
    with open(file_path, "r") as file:
        return yaml.safe_load(file)
```

#### Parameters

- `file_path` (str): Path to the YAML file

#### Returns

- `dict`: The loaded configuration as a dictionary

### format_markdown

Format markdown content for better presentation.

```python
def format_markdown(content, title):
    formatted_content = f"""# {title}

{content}"""
    return formatted_content
```

#### Parameters

- `content` (str): Markdown content to format
- `title` (str): Title for the formatted content

#### Returns

- `str`: The formatted markdown content 