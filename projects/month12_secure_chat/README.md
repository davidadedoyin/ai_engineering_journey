# Secure chat app

This project is a simple example of an authenticated local chat endpoint. It checks for an API key in the request headers before allowing access.

## Goal

The app demonstrates a beginner-friendly auth layer: secret management, header validation, and a protected route.

## How to run

```bash
cd ai-engineering-journey
.venv\Scripts\python.exe -m uvicorn projects.month12_secure_chat.app:app --host 127.0.0.1 --port 8010 --reload
```

## Example request

```bash
curl.exe http://127.0.0.1:8010/chat -H "X-API-Key: demo-secret"
```

## Limitations

This is a teaching example, not a production-grade auth system. It is intentionally simple and meant to illustrate the pattern.
