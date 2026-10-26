# LLM assistant

This project is a lightweight model-backed assistant that accepts a user prompt and returns a simple structured response.

## Goal

The app demonstrates the model request flow: validate input, send prompt to the model provider, and return the output in JSON.

## How to run

```bash
cd ai-engineering-journey
.venv\Scripts\python.exe -m uvicorn projects.month7_llm_assistant.app:app --host 127.0.0.1 --port 8005 --reload
```

## Example request

```json
{
  "message": "Explain what precision means in a classification model."
}
```

## Example response

```json
{
  "answer": "Precision tells us how often predicted positive results are actually correct."
}
```

## Limitations

This project is a learning prototype. It does not include production guardrails, authentication, or a real provider configuration by default.
