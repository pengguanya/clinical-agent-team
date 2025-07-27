from langchain_core.messages import AIMessage, HumanMessage
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_anthropic import ChatAnthropic
from supabase import create_client, Client
from dotenv import load_dotenv
import requests
import json
import time
import os

load_dotenv()
model = os.getenv('LLM_MODEL', 'gpt-4o')
embedding_model = os.getenv('EMBEDDING_MODEL', 'text-embedding-3-small')
supabase_url = os.getenv('SUPABASE_URL')
supabase_service_secret = os.getenv('SUPABASE_SERVICE_KEY')

# Initialize OpenAI, OpenAI Client for embeddings, and Supabase clients
llm = ChatOpenAI(model=model) if "gpt" in model.lower() else ChatAnthropic(model=model)
embeddings = OpenAIEmbeddings(model=embedding_model, dimensions=1536)
supabase: Client = create_client(supabase_url, supabase_service_secret)

def fetch_workflow(workflow_id):
    """
    Retrieves n8n workflow template from their public API.

    Args:
        workflow_id: Identifier of the workflow template to fetch

    Returns:
        dict: Workflow template data if found, None if not found or on error
    """    
    url = f"https://api.n8n.io/api/templates/workflows/{workflow_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

def process_workflow(workflow_data):
    """
    Converts n8n workflow data into an HTML component string.
    
    Takes raw workflow data, escapes special characters, and wraps in n8n-demo 
    component tags.

    Args:
        workflow_data: Dictionary containing workflow template data from n8n API

    Returns:
        str: HTML component string with escaped workflow data,
            None if workflow_data is invalid

    Example:
        "<n8n-demo workflow='{\"nodes\":[...]}></n8n-demo>"
    """    
    if workflow_data and 'workflow' in workflow_data and 'workflow' in workflow_data['workflow']:
        workflow = workflow_data['workflow']['workflow']
        # Convert the workflow to a JSON string
        workflow_json = json.dumps(workflow)
        # Escape single quotes in the JSON string
        workflow_json_escaped = workflow_json.replace("'", "\\'")
        # Create the n8n-demo component string
        return f"<n8n-demo workflow='{workflow_json_escaped}'></n8n-demo>"
    return None

def check_workflow_legitimacy(workflow_json):
    """
    Uses LLM to assess if an n8n workflow is legitimate vs test/spam.
    
    Prompts LLM to analyze workflow structure and patterns to determine validity.

    Args:
        workflow_json: JSON string containing the n8n workflow data

    Returns:
        str: 'GOOD' for legitimate workflows, 'BAD' for test/spam workflows
    """    
    legitimacy_prompt = f"""
    You are an expert in n8n workflows. Analyze the following workflow JSON and determine if it's a legitimate workflow or a test/spam one.
    Output only GOOD if it's a legitimate workflow, or BAD if it's a test/spam workflow.

    Workflow JSON:
    {workflow_json}

    Output (GOOD/BAD):
    """
    return llm.invoke([HumanMessage(content=legitimacy_prompt)]).content.strip()

def analyze_workflow(workflow_json):
    """
    Uses LLM to perform comprehensive workflow analysis.

    Generates three analyses:
    1. Overall workflow purpose and functionality
    2. Node configuration and connections
    3. Potential variations and expansions

    Args:
        workflow_json: JSON string containing the n8n workflow data

    Returns:
        list[str]: Three analysis results in order:
            [purpose_summary, node_analysis, expansion_suggestions]
    """    
    summary_prompts = [
        f"""
        Summarize what the following n8n workflow is accomplishing:
        {workflow_json}
        Summary:
        """,
        f"""
        Summarize all the nodes used in the following n8n workflow and how they are connected:
        {workflow_json}
        Summary:
        """,
        f"""
        Based on the following n8n workflow, suggest similar workflows that could be made using this as an example. 
        Consider different services but similar setups, and ways the workflow could be expanded:
        {workflow_json}
        Suggestions:
        """
    ]
