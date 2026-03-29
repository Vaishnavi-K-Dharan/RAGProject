from PIL import Image
import pandas as pd
from sentence_transformers import SentenceTransformer
from preprocessors.query_interpreter import QueryInterpreter

class InputAdapter:
    def __init__(self):
        self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.interpreter = QueryInterpreter()
    
    def preprocess(self, input_data):
        if isinstance(input_data, str):
            return {"type": "text", "data": input_data}
        elif isinstance(input_data, Image.Image):
            return {"type": "image", "data": "Image detected"}
        elif isinstance(input_data, pd.DataFrame):
            return {"type": "table", "data": input_data.to_json()}
        return {"type": "unknown", "data": str(input_data)}
