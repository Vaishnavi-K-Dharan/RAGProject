from langgraph.graph import StateGraph, END
from typing import TypedDict, Dict, List
from config import Config
from agents.planner import PlannerAgent
from retrievers.vector_retriever import VectorRetriever
# ... import other components

class AgentState(TypedDict):
    query: str
    tasks: List[Dict]
    retrieved: Dict
    answer: str
    confidence: float

config = Config()
planner = PlannerAgent(config)
vector_retriever = VectorRetriever(config)

def planner_node(state):
    tasks = planner.plan(state["query"])
    return {"tasks": tasks}

def retrieve_node(state):
    docs = vector_retriever.retrieve(state["query"])
    return {"retrieved": {"vector": [d.page_content for d in docs]}}

workflow = StateGraph(AgentState)
workflow.add_node("planner", planner_node)
workflow.add_node("retrieve", retrieve_node)
workflow.set_entry_point("planner")
workflow.add_edge("planner", "retrieve")
workflow.add_edge("retrieve", END)

app = workflow.compile()
