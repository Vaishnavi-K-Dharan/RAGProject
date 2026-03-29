from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader

class VectorRetriever:
    def __init__(self, config, docs_path="data/sample_docs.txt"):
        self.embeddings = OpenAIEmbeddings(api_key=config.OPENAI_API_KEY)
        loader = TextLoader(docs_path)
        docs = loader.load()
        self.vectorstore = FAISS.from_documents(docs, self.embeddings)
    
    def retrieve(self, query: str, k=3):
        return self.vectorstore.similarity_search(query, k=k)
