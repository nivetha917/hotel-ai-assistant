from app.rag.retriever import Retriever
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Load Retriever once
retriever = Retriever()

# Load LLM once
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0
)

# Prompt
prompt = ChatPromptTemplate.from_template(
"""
You are a Hotel AI Assistant.

Answer ONLY using the information provided in the context.

If the answer is not available, say:

"I couldn't find that information in the hotel document."

Context:
{context}

Question:
{question}
"""
)


def ask_question(question: str):
    """
    Answer hotel questions using RAG.
    """

    # Retrieve relevant chunks
    chunks = retriever.search(question)

    context = "\n\n".join(chunks)

    messages = prompt.format_messages(
        context=context,
        question=question
    )

    response = llm.invoke(messages)

    return response.content


if __name__ == "__main__":

    question = input("Ask your question: ")

    answer = ask_question(question)

    print("\nFinal Answer:\n")
    print(answer)