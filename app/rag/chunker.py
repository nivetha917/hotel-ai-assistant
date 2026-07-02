from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.rag.loader import load_pdf


def get_chunks(pdf_path):

    text = load_pdf(pdf_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    return splitter.split_text(text)


if __name__ == "__main__":

    chunks = get_chunks("data/hotel_rag_document_v2.pdf")

    print(f"Total Chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks):
        print("=" * 50)
        print(f"Chunk {i+1}")
        print("=" * 50)
        print(chunk[:300])