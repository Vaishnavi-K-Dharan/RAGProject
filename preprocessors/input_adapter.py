import streamlit as st
from transformers import pipeline, CLIPProcessor, CLIPModel
from PIL import Image
import pandas as pd
import pytesseract

def detect_modality(input_data):
    if isinstance(input_data, str):
        return "text"
    elif isinstance(input_data, Image.Image):
        return "image"
    elif isinstance(input_data, (pd.DataFrame, list)):
        return "tabular"
    return "unknown"

def preprocess_image(img):
    ocr_pipe = pipeline("document-question-answering", model="impira/layoutlm-document-qa")
    text = pytesseract.image_to_string(img)
    clip_model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
    processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
    embedding = processor(images=img, return_tensors="pt")
    return {"text": text, "embedding": embedding}

# Usage in app: modality = detect_modality(uploaded_file)
