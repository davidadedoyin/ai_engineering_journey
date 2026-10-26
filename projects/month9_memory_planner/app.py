from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Memory Planner")


class PlannerRequest(BaseModel):
    goal: str
    history: list[str] = []


def plan_goal(goal: str, history: list[str]) -> list[str]:
    lower = goal.lower()
    if "python" in lower:
        return [
            "Review Python basics and syntax",
            "Practice small projects with functions and files",
            "Add a polished project to a portfolio README",
        ]
    if "rag" in lower or "retrieval" in lower:
        return [
            "Build a knowledge base or FAQ document set",
            "Add a retrieval step to rank relevant documents",
            "Generate a grounded answer using the retrieved context",
        ]
    if "portfolio" in lower or "project" in lower:
        return [
            "List the portfolio goals and target audience",
            "Choose one or two working projects to showcase",
            "Document the process and the verification results",
        ]
    if history:
        return [
            "Review the past work and identify what is already validated",
            "Pick the next missing learning milestone",
            "Create an honest progress update with verification notes",
        ]
    return [
        "Define the main learning objective",
        "Break it into small milestones",
        "Validate each milestone with a real script or project output",
    ]


@app.get("/")
def root():
    return {"message": "Memory planner is running."}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/plan")
def plan(request: PlannerRequest):
    steps = plan_goal(request.goal, request.history)
    return {"goal": request.goal, "steps": steps}
