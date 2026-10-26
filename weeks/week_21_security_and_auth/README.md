# Week 21: Security and auth

## Analogy

A deployed AI service is not just a model; it is also a public service. Security is the difference between a helpful tool and an exposed endpoint.

## Mon: API security basics

In production, do not expose internal tools to the public by default. You need:
- authentication
- authorization
- rate limiting
- secret management

## Tue: environment variables and secrets

Store real credentials in `.env` and never commit them to Git.

```python
import os
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    print("No API key configured")
```

## Wed: access keys and auth patterns

Common patterns include:
- API keys in headers
- bearer tokens
- reverse-proxy auth
- OAuth flows for user apps

For a beginner app, an API key check is a useful first step.

## Thu: request validation

Validate input before using it in model calls or database lookups.

```python
from pydantic import BaseModel

class PromptRequest(BaseModel):
    message: str
```

## Friday challenge

Create a tiny FastAPI app that checks for a valid API key in the request header before answering.

## Saturday project

Build a security wrapper for the flagship app in `projects/month12_secure_chat/`.

## Did it stick? Repeat checklist

- I can explain why `.env` matters for secrets.
- I can describe a simple API-key pattern.
- I can explain why validation matters before using input.
- I can explain the difference between auth and authorization.
