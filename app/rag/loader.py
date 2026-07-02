import fitz


def load_pdf(pdf_path):

    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    return text


if __name__ == "__main__":

    pdf_path = "data/hotel_rag_document_v2.pdf"

    text = load_pdf(pdf_path)

    print(text)