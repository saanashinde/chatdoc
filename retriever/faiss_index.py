import faiss
import numpy as np

class FAISSRetriever:
    def __init__(self, embeddings, chunks):
        self.index = faiss.IndexFlatL2(embeddings.shape[1])
        self.index.add(embeddings)
        self.chunks = chunks

    def retrieve(self, query_embedding, k=3):
        D, I = self.index.search(query_embedding, k)
        return [self.chunks[i] for i in I[0]]
