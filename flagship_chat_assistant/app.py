import re

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Flagship Chat Assistant")

# Local knowledge base for a lightweight retrieval prototype.
KNOWLEDGE_BASE = [
    {
        "title": "AI engineering roadmap",
        "content": "This repository is a beginner to advanced AI engineering learning path. It covers Python, data analysis, machine learning, model evaluation, FastAPI, NLP, RAG, and deployment.",
    },
    {
        "title": "Python foundations",
        "content": "Python is the foundation for AI engineering. Learn variables, loops, functions, classes, files, and Git before moving into data science and ML topics.",
    },
    {
        "title": "Model evaluation",
        "content": "Classification models need precision, recall, F1, confusion matrices, and cross-validation. Look at train and test performance to detect overfitting or underfitting.",
    },
    {
        "title": "FastAPI",
        "content": "FastAPI lets you publish services with JSON endpoints. A simple app can expose /health and /predict endpoints and can later be connected to a model or retrieval layer.",
    },
    {
        "title": "RAG",
        "content": "Retrieval augmented generation uses a local knowledge base or vector store to fetch relevant documents before generating an answer. This helps ground responses in context.",
    },
    {
        "title": "Safety",
        "content": "Keep secrets in .env and do not commit API keys. Mark work as unverified when you cannot run it locally. Always be honest about what was validated.",
    },
]


class ChatRequest(BaseModel):
    message: str
    max_results: int = 3


def normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9\s]", " ", text.lower())


def tokenize(text: str):
    return normalize(text).split()


def score_document(question: str, document: dict) -> int:
    question_tokens = set(tokenize(question))
    if not question_tokens:
        return 0
    doc_tokens = set(tokenize(document["content"]))
    title_tokens = set(tokenize(document["title"]))
    overlap = len(question_tokens & doc_tokens)
    title_bonus = 2 if question_tokens & title_tokens else 0
    return overlap + title_bonus


def retrieve_documents(question: str, max_results: int = 3):
    ranked = []
    for document in KNOWLEDGE_BASE:
        ranked.append((score_document(question, document), document))
    ranked.sort(key=lambda item: item[0], reverse=True)
    return [(document["title"], document["content"]) for _, document in ranked[:max_results] if _ > 0]


def build_answer(question: str, context: list[tuple[str, str]]) -> str:
    text = " ".join(content for _, content in context)
    lower_question = question.lower()

    if "python" in lower_question:
        return "Python is the foundation of this roadmap. Start with variables, loops, functions, files, and classes before moving to data work and ML."
    if "model" in lower_question or "evaluation" in lower_question or "precision" in lower_question or "f1" in lower_question:
        return "Model evaluation should use precision, recall, F1, confusion matrices, and validation splits. Comparing train and test scores helps catch overfitting and underfitting."
    if "fastapi" in lower_question or "api" in lower_question:
        return "FastAPI is a lightweight way to expose JSON endpoints and connect a model or service to a client. The pattern is straightforward: route functions return structured Python objects."
    if "rag" in lower_question or "retrieval" in lower_question or "knowledge" in lower_question:
        return "A retrieval system finds the most relevant documents and then uses that context to craft an answer. This kind of grounded answer is more reliable than guessing from a single prompt."
    if "safety" in lower_question or "secret" in lower_question or "env" in lower_question:
        return "Keep secrets in a local .env file and never commit them to the repo. Validate changes honestly and mark anything unverified as such."
    if context:
        return f"Based on the local project material: {text[:300]}"
    return "I could not find a strong match in the local knowledge base. Ask about Python, model evaluation, FastAPI, RAG, or project safety."


@app.get("/health")
def health():
    return {"status": "ok", "mode": "prototype-local-retrieval"}


@app.get("/documents")
def documents():
    return {"documents": KNOWLEDGE_BASE}


@app.post("/chat")
def chat(request: ChatRequest):
    matches = retrieve_documents(request.message, request.max_results)
    answer = build_answer(request.message, matches)
    return {
        "answer": answer,
        "sources": [{"title": title} for title, _ in matches],
    }
