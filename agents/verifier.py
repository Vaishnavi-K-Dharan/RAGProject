from transformers import pipeline

class VerifierAgent:
    def __init__(self):
        self.nli = pipeline("zero-shot-classification", 
                          model="facebook/bart-large-mnli")
    
    def verify(self, answer: str, sources: list) -> tuple:
        source_text = " ".join(sources[:2])
        result = self.nli(answer, source_text, 
                         candidate_labels=["entailment", "contradiction"])
        confidence = result["scores"][0]
        return answer, confidence
