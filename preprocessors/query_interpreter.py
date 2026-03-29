class QueryInterpreter:
    def interpret(self, text: str):
        # Simplified intent classification
        intents = ["information_retrieval"] if "what" in text.lower() else ["advisory"]
        return {"intents": intents, "entities": text.split()}
