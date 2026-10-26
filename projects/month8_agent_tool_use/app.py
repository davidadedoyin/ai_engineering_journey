from __future__ import annotations

import ast
import operator

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Agent Tool Use")


class MessageRequest(BaseModel):
    message: str


def explain_concept(text: str) -> str:
    if "precision" in text:
        return "Precision tells us how often predicted positives are actually correct."
    if "recall" in text:
        return "Recall shows how many real positives were found by the model."
    if "fastapi" in text:
        return "FastAPI is a Python web framework for building APIs quickly."
    return "This topic is best explained by breaking it into simple steps and examples."


def safe_calculate(expression: str):
    expression = expression.strip()
    if not expression:
        return None
    try:
        node = ast.parse(expression, mode="eval")
    except SyntaxError:
        return None

    allowed_names = {"__builtins__": {} }
    ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    def eval_node(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.BinOp) and type(node.op) in ops:
            return ops[type(node.op)](eval_node(node.left), eval_node(node.right))
        if isinstance(node, ast.UnaryOp) and type(node.op) in ops:
            return ops[type(node.op)](eval_node(node.operand))
        raise ValueError("unsupported expression")

    try:
        return eval_node(node.body)
    except Exception:
        return None


def summarize(text: str) -> str:
    words = text.split()
    return " ".join(words[:12]) + ("..." if len(words) > 12 else "")


@app.get("/")
def root():
    return {"message": "Agent tool-use prototype is running."}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/route")
def route(request: MessageRequest):
    text = request.message.lower()

    if "calculate" in text:
        expr = request.message.lower().replace("calculate", "").replace("what is", "").strip()
        if expr:
            value = safe_calculate(expr)
            if value is not None:
                return {"tool": "calculator", "result": value}

    if any(op in text for op in ["*", "/", "+", "-"]):
        value = safe_calculate(request.message)
        if value is not None:
            return {"tool": "calculator", "result": value}

    if "explain" in text or "what is" in text:
        return {"tool": "concept_explainer", "result": explain_concept(request.message)}

    if "summarize" in text:
        return {"tool": "summarizer", "result": summarize(request.message)}

    return {"tool": "fallback", "result": "I can explain, calculate, or summarize a request."}
