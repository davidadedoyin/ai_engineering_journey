# Agent tool-use assistant

This project demonstrates a very small tool-calling workflow. The assistant can decide which local tool to use based on a user request.

## Goal

The app supports a few built-in actions:
- explain a concept
- calculate a number
- summarize a message

## How to run

```bash
cd ai-engineering-journey
.venv\Scripts\python.exe -m uvicorn projects.month8_agent_tool_use.app:app --host 127.0.0.1 --port 8006 --reload
```

## Example request

```json
{
  "message": "Calculate 12 * 9"
}
```

## Example response

```json
{
  "tool": "calculator",
  "result": 108
}
```

## Limitations

This is a teaching prototype. It is not a general-purpose autonomous agent and does not include external tool providers or persistence.
