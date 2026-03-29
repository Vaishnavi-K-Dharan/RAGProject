import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
    NEO4J_URI = os.getenv("NEO4J_URI", "neo4j+s://demo.neo4jlabs.com")
    NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "password")
    
    EMBEDDING_MODEL = "text-embedding-3-small"
    LLM_MODEL = "gpt-4o-mini"
    
    # File paths
    SAMPLE_DATA_DIR = "data"
