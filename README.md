
# 🧠 ChatDoc – Document-Based Question-Answering Chatbot

ChatDoc is an AI-powered chatbot that understands and answers questions based on the content of uploaded documents (PDF, DOCX, TXT). It leverages a Retrieval-Augmented Generation (RAG) pipeline using open-source LLMs, embeddings, and FAISS for semantic search.

---

## 🚀 Features

- 📄 Supports PDF, DOCX, and TXT documents
- 🔍 Context-aware question answering using document content
- 🔗 Retrieval-Augmented Generation (RAG) pipeline
- 💬 Chat interface built with Streamlit
- 🧠 Uses sentence embeddings + FAISS for fast and relevant chunk retrieval
- 🪄 Fine-tuned or lightweight LLMs (e.g., Mistral-7B-Instruct, DistilGPT2)

---

## 📂 Project Structure

```

chatdoc/
├── app.py                     # Streamlit interface
├── parser/                   # Document parsers
│   ├── pdf\_parser.py
│   └── docx\_parser.py
├── retriever/                # Embedding and FAISS index logic
│   ├── embedder.py
│   └── faiss\_index.py
├── llm/                      # RAG logic and model interface
│   └── rag\_pipeline.py
├── utils/                    # Text chunking and preprocessing
│   └── chunker.py
├── model/                    # Fine-tuned or preloaded model (optional)
│   └── ...
├── requirements.txt
└── README.md

````

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Language**: Python
- **LLM**: Hugging Face Transformers (e.g., DistilGPT2, Mistral)
- **Embedding**: Sentence Transformers
- **Retriever**: FAISS
- **Document Parsing**: PyMuPDF, python-docx
- **Text Processing**: spaCy

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chatdoc.git
cd chatdoc
````

### 2. Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate      # On Windows
# source venv/bin/activate # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## 📌 Use Case Examples

* 📘 HR Policy document Q\&A
* 📑 Legal document summarization
* 🛠️ Product manual support assistant
* 🎓 Educational materials helper

---

## 📦 Datasets (optional for training)

For fine-tuning your own LLM, you can use:

* [StackOverflow Question-Answer Pairs](https://www.kaggle.com/datasets/sashankpillai/stackoverflow-qa-pairs)
* [SQuAD Dataset](https://rajpurkar.github.io/SQuAD-explorer/)
* [Multilingual QA Dataset (MLQA)](https://github.com/facebookresearch/MLQA)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♀️ Author

**Saana Shinde**
GitHub: [@saanashinde](https://github.com/saanashinde)

---

## 🌐 Demo / Deployment

To deploy:

* Push the project to a public GitHub repo
* Deploy via [Streamlit Community Cloud](https://streamlit.io/cloud)


