# Flagship chat assistant

This folder contains a working prototype of the final AI assistant.

## Current status

The app exposes a local FastAPI service with a health endpoint and a retrieval-based `/chat` endpoint. It is intentionally lightweight and does not require an external API key.

## How it works

- It keeps a small local knowledge base about the roadmap and the project.
- It scores relevant documents by keyword overlap.
- It returns a structured answer with the best matching sources.
- This is a prototype retrieval assistant, not a production LLM deployment.

## Deployment note

A simple Dockerfile is included in this folder as an example of container packaging. It is not a verified production deployment pipeline and should be treated as a teaching scaffold unless you validate it in your environment.

## Limitations

This is a local prototype for learning and demonstration. It does not yet include authentication, logging, vector search, or a cloud LLM provider.
