from __future__ import annotations

import logging
import os
from pathlib import Path

from anthropic import Anthropic, APIConnectionError, APIError, RateLimitError
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

load_dotenv(Path(__file__).resolve().parents[2] / ".env")

app = FastAPI(title="LLM Assistant")
logger = logging.getLogger(__name__)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "").strip()
if ANTHROPIC_API_KEY == "your_api_key_here":
    ANTHROPIC_API_KEY = ""
ANTHROPIC_MODEL = os.getenv("ANTHROPIC_MODEL") or "claude-haiku-5-5"
client = Anthropic(api_key=ANTHROPIC_API_KEY) if ANTHROPIC_API_KEY else None


class MessageRequest(BaseModel):
    message: str


@app.get("/")
def root():
    return {"message": "LLM assistant prototype is running."}


@app.get("/health")
def health():
    return {
        "status": "ok",
        "provider": "anthropic",
        "configured": client is not None,
        "model": ANTHROPIC_MODEL,
    }


@app.post("/answer")
def answer(request: MessageRequest):
    if client is None:
        raise HTTPException(
            status_code=503,
            detail="Anthropic is not configured. Set ANTHROPIC_API_KEY in the repository .env file.",
        )

    try:
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=512,
            system="You are a helpful AI engineering tutor. Answer clearly and simply.",
            messages=[{"role": "user", "content": request.message}],
        )
    except RateLimitError as exc:
        logger.warning("Anthropic rate limit reached.")
        raise HTTPException(status_code=429, detail="The LLM provider rate limit was reached.") from exc
    except APIConnectionError as exc:
        logger.exception("Could not connect to Anthropic.")
        raise HTTPException(status_code=502, detail="Could not connect to the LLM provider.") from exc
    except APIError as exc:
        logger.exception("Anthropic API request failed.")
        raise HTTPException(status_code=502, detail="The LLM provider request failed.") from exc

    answer_text = "\n".join(
        block.text for block in response.content if block.type == "text"
    ).strip()
    if not answer_text:
        raise HTTPException(status_code=502, detail="The LLM provider returned no text.")
    return {"answer": answer_text, "model": response.model}
