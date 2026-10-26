from __future__ import annotations

import os
import re

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Final Chat App")

KNOWLEDGE_BASE = [
    {
        "title": "AI engineering roadmap",
        "content": "This repo covers Python, data analysis, ML, model evaluation, FastAPI, NLP, retrieval, and deployment. A solid project portfolio matters as much as theory.",
    },
    {
        "title": "RAG",
        "content": "Retrieval augmented generation retrieves relevant documents and adds them to the prompt before generating a final answer. This keeps the response grounded in evidence.",
    },
    {
        "title": "Model evaluation",
        "content": "Use train/test splits, precision, recall, F1, and confusion matrices to judge whether a model is trustworthy. Overfitting is a common issue for beginners.",
    },
    {
        "title": "FastAPI",
        "content": "FastAPI lets you expose JSON endpoints quickly and cleanly. It is excellent for serving simple ML services and app prototypes.",
    },
    {
        "title": "Safety",
        "content": "Never commit API keys. Keep secrets in .env, validate your work, and mark anything unverified as such.",
    },
]


class ChatRequest(BaseModel):
    message: str


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9\s]", " ", text.lower())


def retrieve(question: str, max_results: int = 3):
    q_tokens = set(normalize(question).split())
    ranked = []
    for doc in KNOWLEDGE_BASE:
        tokens = set(normalize(doc["content"]).split())
        title_tokens = set(normalize(doc["title"]).split())
        score = len(q_tokens & tokens) + (2 if q_tokens & title_tokens else 0)
        ranked.append((score, doc))
    ranked.sort(key=lambda item: item[0], reverse=True)
    return [(doc["title"], doc["content"]) for score, doc in ranked[:max_results] if score > 0]


def build_local_answer(question: str, context: list[tuple[str, str]]) -> str:
    q = question.lower()
    if "rag" in q:
        return "RAG combines retrieval with generation. It finds the most relevant documents and gives them to the model so the answer is grounded in context."
    if "fastapi" in q:
        return "FastAPI is a lightweight Python API framework. It is often used for simple ML services, helpers, and internal tools."
    if "model" in q and ("evaluate" in q or "evaluation" in q or "precision" in q or "recall" in q or "f1" in q):
        return "Model evaluation should include train/test splits and metrics like precision, recall, F1, and confusion matrices. These help estimate how trustworthy the model is."
    if "python" in q:
        return "Python is the foundation for AI engineering because it is readable and has strong scientific and ML libraries."
    if "secret" in q or "env" in q or "api key" in q:
        return "Keep secrets in a local .env file only. Never commit API keys to the repository."
    if context:
        text = " ".join(content for _, content in context)
        return f"The strongest local context suggests: {text[:250]}"
    return "I am using the local knowledge base for this answer. For a hosted model, configure an API key in .env and connect the provider."


@app.get("/health")
def health():
    return {
        "status": "ok",
        "mode": "local-grounded-prototype",
        "llm_configured": bool(os.getenv("ANTHROPIC_API_KEY")),
    }


@app.post("/chat")
def chat(request: ChatRequest):
    matches = retrieve(request.message)
    answer = build_local_answer(request.message, matches)
    return {"answer": answer, "sources": [{"title": title} for title, _ in matches]}
