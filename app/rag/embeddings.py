from sentence_transformers import SentenceTransformer
from app.rag.chunker import get_chunks


def create_embeddings(pdf_path):
    # Load all chunks
    chunks = get_chunks(pdf_path)

    # Load embedding model
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Generate embeddings
    embeddings = model.encode(chunks)

    return chunks, embeddings


if __name__ == "__main__":

    pdf_path = "data/hotel_rag_document_v2.pdf"

    chunks, embeddings = create_embeddings(pdf_path)

    print(f"Total Chunks: {len(chunks)}")
    print(f"Embedding Shape: {embeddings.shape}")

    print("\nFirst Chunk:\n")
    print(chunks[0])

    print("\nFirst Embedding (first 10 values):\n")
    print(embeddings[0][:10])