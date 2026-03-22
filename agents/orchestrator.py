from transformers import pipeline

nli_pipeline = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def verifier(draft: str, sources: dict):
    for source_type, docs in sources.items():
        result = nli_pipeline(draft, docs[0].page_content, candidate_labels=["entailment", "contradiction"])
        confidence = result["scores"][result["labels"].index("entailment")]
    return confidence > 0.8  # Threshold

def text_agent(state):
    sources = retrieve(state["query"])
    draft = llm.invoke(f"Summarize with citations: {sources}").content
    verified = verifier(draft, sources)
    return {"answer": draft if verified else "Low confidence - recheck", "sources": sources}
