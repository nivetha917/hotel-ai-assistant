import faiss
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer


class Retriever:

    def __init__(self):

        # Load FAISS index
        self.index = faiss.read_index("vectorstore/hotel_index.faiss")

        # Load chunks
        with open("vectorstore/chunks.pkl", "rb") as f:
            self.chunks = pickle.load(f)

        # Load embedding model
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def search(self, query, k=3):

        # Convert question to embedding
        query_embedding = self.model.encode([query])

        query_embedding = np.array(query_embedding).astype("float32")

        # Search similar vectors
        distances, indices = self.index.search(query_embedding, k)

        results = []

        for idx in indices[0]:
            results.append(self.chunks[idx])

        return results


if __name__ == "__main__":

    retriever = Retriever()

    question = input("Ask a question: ")

    results = retriever.search(question)

    print("\nRetrieved Chunks\n")

    for i, chunk in enumerate(results):

        print("=" * 60)
        print(f"Result {i+1}")
        print("=" * 60)
        print(chunk)