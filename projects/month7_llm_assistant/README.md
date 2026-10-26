# LLM assistant

This project is a lightweight Anthropic Claude-backed assistant that accepts a user prompt and returns a structured response.

## Goal

The app validates input, sends it to Anthropic's Messages API, and returns the model response as JSON.

## Configure the provider

From the repository root, create your local `.env` file from the example:

```powershell
Copy-Item .env.example .env
```

Set `ANTHROPIC_API_KEY` in `.env`. Keep the key private; `.env` is ignored by Git. `ANTHROPIC_MODEL` defaults to `claude-haiku-5-5` and can be changed to another model enabled for your Anthropic account.

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
  "answer": "Precision tells us how often predicted positive results are actually correct.",
  "model": "claude-haiku-5-5"
}
```

## Limitations

This project is a learning prototype. Requests to `/answer` use the configured Anthropic API and may incur usage charges. It does not include production guardrails or authentication. Without `ANTHROPIC_API_KEY`, the endpoint returns HTTP 503 rather than a mock answer.
