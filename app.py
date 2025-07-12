import streamlit as st
import os
from parser.pdf_parser import extract_text_from_pdf
from parser.docx_parser import extract_text_from_docx
from utils.chunker import chunk_text
from retriever.embedder import encode_chunks, encode_query
from retriever.faiss_index import FAISSRetriever
from llm.rag_pipeline import generate_answer

st.set_page_config(page_title="ChatDoc", layout="wide")
st.title("📄 ChatDoc – Ask Your Document")

uploaded_file = st.file_uploader("Upload PDF, DOCX, or TXT", type=["pdf", "docx", "txt"])

if uploaded_file:
    file_path = f"temp_{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    if file_path.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith(".docx"):
        text = extract_text_from_docx(file_path)
    elif file_path.endswith(".txt"):
        text = open(file_path, "r", encoding="utf-8").read()
    else:
        st.error("Unsupported file type.")
        st.stop()

    chunks = chunk_text(text)
    embeddings = encode_chunks(chunks)
    retriever = FAISSRetriever(embeddings, chunks)

    st.success("✅ Document parsed. Ask a question!")

    user_query = st.text_input("💬 Ask a question about the document:")
    if user_query:
        query_embedding = encode_query(user_query)
        context_chunks = retriever.retrieve(query_embedding)
        context = "\n".join(context_chunks)
        answer = generate_answer(context, user_query)
        st.markdown(f"**Answer:** {answer}")
