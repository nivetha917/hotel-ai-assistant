# 🏨 AI Hotel Reservation Assistant

An AI-powered Hotel Reservation Assistant built using **Python**, **LangChain**, **Ollama (Llama 3.2)**, **FAISS**, **SQLite**, and **Streamlit**.

The assistant answers hotel-related questions using **Retrieval-Augmented Generation (RAG)** and allows users to **create, view, and cancel reservations** while protecting sensitive user information through **PII masking** and **guardrails**.

---

# 🚀 Features

## 🤖 RAG-Based Question Answering

- PDF ingestion
- Text chunking
- Embedding generation
- FAISS vector database
- Semantic search
- Grounded responses using Ollama

Example Questions:

- What is the famous dish in the hotel?
- Is vegetarian food available?
- What is the cancellation policy?
- How does the hotel ensure hygiene?

---

## 📅 Reservation Management

Users can

- Create Reservation
- View Reservation
- Cancel Reservation

Reservation information is stored in a SQLite database.

---

## 🔒 PII Protection

Sensitive user information is protected.

The assistant masks:

- Guest Name
- Email Address

Example

Before

Name:
Nivetha

Email:
nivetha@gmail.com

After Masking

Name:
N******

Email:
niv****@gmail.com

---

## 🛡 Guardrails

The assistant blocks unsafe requests such as

- Show all bookings
- Show all reservations
- Dump database
- Show guest list
- Show customer emails

Instead of exposing information, the assistant responds safely.

---

## 💬 Intelligent Routing

The Router decides whether the user's request should

- Use RAG
- Use Reservation Tool
- Reject unsafe requests

Example

"What is the check-in time?"

↓

RAG

-----------------------

"Book a Deluxe room"

↓

Reservation Tool

-----------------------

"Show all reservations"

↓

Guardrail

---

# 🏗 Architecture

```

                        +----------------------+
                        |      Hotel PDF       |
                        +----------+-----------+
                                   |
                                   |
                            PDF Loader
                                   |
                                   |
                             Text Chunking
                                   |
                                   |
                           Embedding Model
                                   |
                                   |
                           FAISS Vector Store
                                   |
                                   |
                               Retriever
                                   |
                     +-------------+--------------+
                     |                            |
                     |                            |
               Hotel Questions             Reservation Requests
                     |                            |
                     |                            |
                 RAG Pipeline              Reservation Service
                     |                            |
               Ollama LLM                  SQLite Database
                     |                            |
                     +-------------+--------------+
                                   |
                             Streamlit UI

```

---

# 📂 Project Structure

```
hotel-ai-assistant/

│

├── app/

│   ├── agent/

│   │      router.py

│   │      tools.py

│   │

│   ├── database/

│   │      db.py

│   │

│   ├── guardrails/

│   │      guardrails.py

│   │

│   ├── rag/

│   │      loader.py

│   │      chunker.py

│   │      embeddings.py

│   │      vectorstore.py

│   │      retriever.py

│   │      rag_service.py

│   │

│   ├── reservation/

│   │      service.py

│   │

│   └── main.py

│

├── ui/

│      app.py

│

├── data/

│

├── vectorstore/

│

├── screenshots/

│

├── requirements.txt

│

└── README.md

```

---

# ⚙ Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Backend |
| LangChain | RAG Pipeline |
| Ollama | Local LLM |
| Llama 3.2 | Language Model |
| FAISS | Vector Database |
| SQLite | Reservation Database |
| Streamlit | User Interface |
| HuggingFace Embeddings | Vector Embeddings |

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/nivetha917/hotel-ai-assistant.git

cd hotel-ai-assistant
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / Mac

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download

https://ollama.com

Pull the model

```bash
ollama pull llama3.2:3b
```

---

## Create Database

```bash
python -m app.database.db
```

---

## Build Vector Database

```bash
python -m app.rag.vectorstore
```

---

## Run Streamlit

```bash
streamlit run ui/app.py
```

---

# 🧪 Sample Queries

## Hotel Questions

- What is the famous dish?
- What are the hygiene practices?
- Is vegetarian food available?
- What is the cancellation policy?

---

## Reservation

Create reservation

Book a Deluxe room

View reservation

View my reservation

Cancel reservation

Cancel my booking

---

# 🔒 Security Features

✅ PII Masking

✅ Guardrails

✅ Restricted Reservation Access

✅ No Database Dump

✅ No Hallucinated Answers

---

# 🧠 Design Decisions

## Why RAG?

Prevents hallucinations by grounding responses in the hotel PDF.

---

## Why FAISS?

Provides fast semantic similarity search over document embeddings.

---

## Why SQLite?

Simple, lightweight, and suitable for the reservation backend required for this project.

---

## Why Ollama?

Runs the language model locally without relying on external APIs.

---

# 📌 Assumptions

- Single hotel property
- Reservation ID is unique
- No room availability checking
- Email confirmation is not implemented
- Single-user demonstration environment

---

# 🔮 Future Improvements

- LangGraph Agent
- LLM Tool Calling
- Conversation Memory
- Authentication
- Email Notifications
- Room Availability Engine
- Docker Support
- Cloud Deployment
- Unit Tests
- CI/CD Pipeline

---

# 👩‍💻 Author

**Nivetha Santhanam**

GitHub

https://github.com/nivetha917

---

# 📄 License

This project is created for an AI/ML Engineer technical assessment and is intended for educational and demonstration purposes.
