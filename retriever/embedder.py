from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def encode_chunks(chunks):
    return model.encode(chunks, convert_to_numpy=True)

def encode_query(query):
    return model.encode([query], convert_to_numpy=True)
