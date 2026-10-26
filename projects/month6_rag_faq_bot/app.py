from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="RAG FAQ Bot")

FAQ = [
    {
        "question": "How do I install Python?",
        "answer": "Download Python from python.org and make sure the interpreter is added to your PATH.",
    },
    {
        "question": "How do I create a virtual environment?",
        "answer": "Run python -m venv .venv and then activate it with .venv\\Scripts\\Activate.ps1 on Windows.",
    },
    {
        "question": "How do I deploy a FastAPI app?",
        "answer": "Start it with uvicorn app:app --host 127.0.0.1 --port 8000 and run it behind a server or container for production.",
    },
    {
        "question": "What is retrieval augmented generation?",
        "answer": "RAG combines a search step with an LLM so the model can answer using the most relevant retrieved documents.",
    },
    {
        "question": "How do I use the repo safely?",
        "answer": "Keep secrets in .env, never commit them, and mark anything unverified as such.",
    },
]


class FAQRequest(BaseModel):
    question: str


def retrieve(question: str, limit: int = 2):
    q = question.lower()
    scored = []
    for item in FAQ:
        score = 0
        for term in q.split():
            if term in item["question"].lower():
                score += 2
            if term in item["answer"].lower():
                score += 1
        scored.append((score, item))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [item for _, item in scored[:limit] if _ > 0]


@app.get("/")
def root():
    return {"message": "RAG FAQ bot is running."}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(request: FAQRequest):
    matches = retrieve(request.question)
    if not matches:
        return {
            "answer": "I could not find a close match in the FAQ. Try asking about Python setup, virtual environments, FastAPI, or retrieval.",
            "sources": [],
        }

    answer = matches[0]["answer"]
    return {
        "answer": answer,
        "sources": [{"question": item["question"]} for item in matches],
    }
