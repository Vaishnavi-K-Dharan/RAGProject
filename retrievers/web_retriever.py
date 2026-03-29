from tavily import TavilyClient

class WebRetriever:
    def __init__(self, config):
        self.client = TavilyClient(api_key=config.TAVILY_API_KEY)
    
    def retrieve(self, query: str):
        return self.client.search(query=query, max_results=3)
