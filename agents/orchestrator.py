from langchain_openai import ChatOpenAI

class OrchestratorAgent:
    def __init__(self, config):
        self.llm = ChatOpenAI(api_key=config.OPENAI_API_KEY, model=config.LLM_MODEL)
    
    def generate(self, context: str, query: str) -> str:
        prompt = f"""
        Context: {context}
        Query: {query}
        
        Answer with citations:
        """
        return self.llm.invoke(prompt).content
