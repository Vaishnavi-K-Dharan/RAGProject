import streamlit as st
from config import Config
from preprocessors.input_adapter import InputAdapter
from graph import app

st.set_page_config(page_title="Agentic RAG", layout="wide")
config = Config()
adapter = InputAdapter()

st.title("Multimodal Agentic RAG")
st.info("Upload files or enter query. Update .env with API keys.")

col1, col2 = st.columns([1, 3])

with col1:
    input_type = st.selectbox("Input:", ["Text", "Image", "CSV/Table"])
    if input_type == "Text":
        query = st.text_area("Query")
        if st.button("Process") and query:
            with col2:
                state = {"query": query}
                result = app.invoke(state)
                st.success(result["answer"])
    
    uploaded_file = st.file_uploader("Or upload file", type=["txt", "csv", "jpg", "png"])
    if uploaded_file:
        input_data = adapter.preprocess(uploaded_file.read())
        st.json(input_data)

st.sidebar.markdown("### Setup\n1. Copy `.env.example` to `.env`\n2. Add API keys\n3. `pip install -r requirements.txt`\n4. `streamlit run app.py`")
