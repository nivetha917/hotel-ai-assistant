import faiss
import numpy as np
import pickle

from app.rag.embeddings import create_embeddings


def build_vector_store(pdf_path):

    # Generate chunks and embeddings
    chunks, embeddings = create_embeddings(pdf_path)

    # Convert embeddings to float32 (required by FAISS)
    embeddings = np.array(embeddings).astype("float32")

    # Create FAISS index
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    # Add embeddings
    index.add(embeddings)

    # Save FAISS index
    faiss.write_index(index, "vectorstore/hotel_index.faiss")

    # Save chunks separately
    with open("vectorstore/chunks.pkl", "wb") as f:
        pickle.dump(chunks, f)

    return index, chunks


if __name__ == "__main__":

    index, chunks = build_vector_store("data/hotel_rag_document_v2.pdf")

    print("Vector Store Created Successfully!")

    print(f"Number of vectors: {index.ntotal}")