from langchain_community.vectorstores import Weaviate
from langchain_community.graphs import Neo4jGraph
from tavily import TavilyClient

weaviate_client = Weaviate(client=weaviate.connect_to_local())
vector_store = Weaviate.from_texts(["sample docs"], embedding="text-embedding-3-small")

neo4j_graph = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USER, password=NEO4J_PASSWORD)

tavily = TavilyClient(api_key=TAVILY_API_KEY)

def retrieve(query: str):
    vector_docs = vector_store.similarity_search(query, k=3)
    kg_results = neo4j_graph.query(f"MATCH (n)-[r]->(m) WHERE n.name CONTAINS '{query}' RETURN n,r,m")
    web_results = tavily.search(query=query, max_results=3)
    return {"vector": vector_docs, "kg": kg_results, "web": web_results}
