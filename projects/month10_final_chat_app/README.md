# Final chat app prototype

This project wraps the learning journey into a more complete local chat experience.

## Goal

The app retrieves relevant knowledge, builds a grounded prompt, and returns a final answer with sources.

## How to run

```bash
cd ai-engineering-journey
.venv\Scripts\python.exe -m uvicorn projects.month10_final_chat_app.app:app --host 127.0.0.1 --port 8008 --reload
```

## Example request

```json
{
  "message": "What is RAG?"
}
```

## Example response

```json
{
  "answer": "RAG combines retrieval with generation so the model answers from relevant context.",
  "sources": ["RAG"]
}
```

## Limitations

This is a local prototype. It uses keyword-based retrieval and a local answer generator. It is not yet connected to a hosted LLM provider or a vector database.
