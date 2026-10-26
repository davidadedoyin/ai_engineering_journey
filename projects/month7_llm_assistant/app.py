from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="LLM Assistant")


class MessageRequest(BaseModel):
    message: str


PROMPT_TEMPLATE = """
You are a helpful AI engineering tutor.
Answer clearly and simply.
User question: {message}
"""


def mock_response(message: str) -> str:
    text = message.lower()
    if "precision" in text:
        return "Precision tells us how often predicted positives are actually correct. It is useful when false positives are costly."
    if "recall" in text:
        return "Recall measures how many true positives the model successfully found. It is useful when false negatives are costly."
    if "fastapi" in text:
        return "FastAPI is a Python framework for building APIs quickly. It uses Python type hints and returns JSON responses naturally."
    if "rag" in text:
        return "RAG combines retrieval with generation so the model can answer from relevant, grounded context instead of guessing."
    if "python" in text:
        return "Python is the main language used in AI engineering because it is readable, flexible, and has strong ML libraries."
    return "The model would answer this by using the project context and a clear explanation tailored to a beginner-friendly AI engineering learner."


@app.get("/")
def root():
    return {"message": "LLM assistant prototype is running."}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/answer")
def answer(request: MessageRequest):
    response = mock_response(request.message)
    return {"answer": response}
