
from langchain_openai import ChatOpenAI
from typing import List
from dataclasses import dataclass

@dataclass
class Task:
    type: str
    description: str
    entity: str = None

class PlannerAgent:
    def __init__(self, config):
        self.llm = ChatOpenAI(api_key=config.OPENAI_API_KEY, model=config.LLM_MODEL)
    
    def plan(self, query: str) -> List[Task]:
        prompt = f"""
        Decompose query into subtasks:
        "{query}"
        
        Return JSON: [{{"type": "RETRIEVE", "description": "..."}}, ...]
        """
        response = self.llm.invoke(prompt)
        # Parse response (simplified)
        tasks = [Task("RETRIEVE", f"Fetch data for {query}")]
        return tasks
