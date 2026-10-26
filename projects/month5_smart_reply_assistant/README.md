# Smart reply assistant

This project creates a lightweight reply generator for common customer support and chat messages.

## Goal

The app reads the user message and suggests a short, helpful reply using a simple rule-based approach.

## How to run

```bash
cd ai-engineering-journey
.venv\Scripts\python.exe -m uvicorn projects.month5_smart_reply_assistant.app:app --host 127.0.0.1 --port 8003 --reload
```

## Example request

```json
{
  "message": "Thanks for the help!"
}
```

## Example response

```json
{
  "reply": "You're very welcome! Happy to help.",
  "category": "thanks"
}
```

## Limitations

This is a rule-based prototype for learning. It is not a full LLM-powered assistant and does not handle every possible message with perfect nuance.
