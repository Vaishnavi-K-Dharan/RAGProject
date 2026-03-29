from langchain_community.graphs import Neo4jGraph

class KGRetriever:
    def __init__(self, config):
        self.kg = Neo4jGraph(
            url=config.NEO4J_URI,
            username=config.NEO4J_USER,
            password=config.NEO4J_PASSWORD
        )
    
    def retrieve(self, query: str):
        cypher = f"""
        MATCH (n)-[r]->(m)
        WHERE toLower(n.name) CONTAINS toLower($query)
        RETURN n,r,m LIMIT 5
        """
        return self.kg.query(cypher, {"query": query})
