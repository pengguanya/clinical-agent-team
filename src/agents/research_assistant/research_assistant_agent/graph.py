from langgraph.graph import END, START, StateGraph   

from research_assistant_agent.schema import (
    InterviewState,
    ResearchGraphState,
)
from research_assistant_agent.nodes import (
    create_analysts,
    human_feedback,
    generate_question,
    search_web,
    search_wikipedia,   
    generate_answer,
    save_interview,
    write_section,
    route_messages,
    initiate_all_interviews,
    write_report,
    write_introduction,
    write_conclusion,
    finalize_report,
)

## Interview Graph

# Add nodes and edges 
interview_builder = StateGraph(InterviewState)
interview_builder.add_node("ask_question", generate_question)
interview_builder.add_node("search_web", search_web)
interview_builder.add_node("search_wikipedia", search_wikipedia)
interview_builder.add_node("answer_question", generate_answer)
interview_builder.add_node("save_interview", save_interview)
interview_builder.add_node("write_section", write_section)

