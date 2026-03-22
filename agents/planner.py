from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from typing import TypedDict, List

class State(TypedDict):
    query: str
    subtasks: List[str]
    intent: str

llm = ChatOpenAI(model="gpt-4o-mini")

def planner_node(state: State):
    prompt = f"Decompose '{state['query']}' into subtasks: retrieve, analyze, summarize."
    subtasks = llm.invoke(prompt).content.split("\n")
    return {"subtasks": subtasks, "intent": "reasoning"}

graph = StateGraph(State)
graph.add_node("planner", planner_node)
graph.set_entry_point("planner")
graph.add_edge("planner", END)
app = graph.compile()
