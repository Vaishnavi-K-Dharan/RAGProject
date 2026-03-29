# Multimodal Agentic RAG Framework

# Folder Structure
multimodal-agentic-rag/
├── agents/          # Planner, retriever, verifier agents
├── retrievers/      # Vector, KG, web
├── preprocessors/   # Modality detection/OCR
├── verifier/        # NLI checks
├── graph.py         # LangGraph workflow
├── app.py           # Streamlit UI
├── data/            # Sample KG/CSV/images
└── requirements.txt


## Quick Start
1. `cp .env.example .env` and add keys
2. `pip install -r requirements.txt`
3. `streamlit run app.py`

## Features
- Multimodal: Text/Image/Table
- Hybrid Retrieval: Vector/KG/Web  
- Agentic: LangGraph orchestration
- Verified: NLI fact-checking

## Architecture
Preprocess → Plan → Retrieve → Generate → Verify
