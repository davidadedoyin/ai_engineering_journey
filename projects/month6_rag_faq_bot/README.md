# RAG FAQ bot

This project is a small retrieval-based FAQ assistant. It stores short Q&A pairs and retrieves the most relevant ones based on the user question before generating a final answer.

## Goal

The app answers common project questions with a grounded retrieval step instead of guessing.

## How to run

```bash
cd ai-engineering-journey
.venv\Scripts\python.exe -m uvicorn projects.month6_rag_faq_bot.app:app --host 127.0.0.1 --port 8004 --reload
```

## Example request

```json
{
  "question": "How do I create a virtual environment?"
}
```

## Example response

```json
{
  "answer": "Run python -m venv .venv and then activate it with .venv\\Scripts\\Activate.ps1 on Windows.",
  "sources": [
    {
      "question": "How do I create a virtual environment?"
    }
  ]
}
```

## Limitations

This is a beginner RAG prototype. It uses simple keyword matching rather than a real embedding model or vector database.
