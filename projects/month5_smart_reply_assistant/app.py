from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Smart Reply Assistant")


class MessageRequest(BaseModel):
    message: str


def suggest_reply(message: str) -> tuple[str, str]:
    text = message.lower().strip()

    if not text:
        return ("Please send a message so I can suggest a reply.", "empty")
    if "hello" in text or "hi" in text or "hey" in text:
        return ("Hello! How can I help you today?", "greeting")
    if "thanks" in text or "thank you" in text or "appreciate" in text:
        return ("You're very welcome! Happy to help.", "thanks")
    if "sorry" in text or "apolog" in text:
        return ("No worries. Thanks for letting me know, and I appreciate your patience.", "apology")
    if "problem" in text or "issue" in text or "broken" in text or "not working" in text:
        return ("Thanks for reporting that. I can help troubleshoot the issue. Please share the exact error or behavior.", "issue")
    if "bye" in text or "goodbye" in text or "see you" in text:
        return ("Goodbye! Take care and talk soon.", "goodbye")
    if "question" in text or "how" in text or "what" in text:
        return ("Happy to help. Please share a little more detail so I can answer accurately.", "question")
    if "love" in text or "great" in text or "amazing" in text or "excellent" in text:
        return ("I'm glad you feel that way! Thank you for the kind words.", "positive")
    return ("Thanks for the message. I’m here to help and can assist with more details if needed.", "neutral")


@app.get("/")
def root():
    return {"message": "Smart reply assistant is running."}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/suggest-reply")
def suggest_reply_endpoint(request: MessageRequest):
    reply, category = suggest_reply(request.message)
    return {"reply": reply, "category": category}
