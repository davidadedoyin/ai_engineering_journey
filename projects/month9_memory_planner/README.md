# Memory planner

This project demonstrates a minimal planning assistant that keeps a short memory of prior tasks and proposes the next step.

## Goal

The app stores a tiny conversation memory and breaks a goal into actionable steps.

## How to run

```bash
cd ai-engineering-journey
.venv\Scripts\python.exe -m uvicorn projects.month9_memory_planner.app:app --host 127.0.0.1 --port 8007 --reload
```

## Example request

```json
{
  "goal": "Learn AI engineering and build a portfolio",
  "history": ["User wants to learn Python", "User built a Titanic API"]
}
```

## Example response

```json
{
  "steps": [
    "Review Python fundamentals",
    "Build a simple model project",
    "Package the work in a portfolio README"
  ]
}
```

## Limitations

This is a teaching prototype. It is intentionally simple and does not use a persistent database or an external model API.
