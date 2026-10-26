# Week 16: LLM and API integration

## Analogy

A model is only useful when it can do real work, not just sit in a notebook. API integration connects the model to real software flows.

## Mon: what is an LLM API?

An LLM API exposes a model through a network endpoint. This allows your app to send a prompt and receive a completion.

Typical flow:
- app sends messages to API
- model reads them
- model returns text
- app uses that response in a workflow

## Tue: prompt structure

A good prompt includes:
- task context
- constraints
- expected output format
- examples when helpful

```python
prompt = """
You are a helpful teaching assistant.
Your job is to explain AI engineering in simple language.
Keep the answer to 3 paragraphs.
"""
print(prompt)
```

## Wed: system vs user messages

In chat APIs, messages are often separated into roles:
- system: overall behavior
- user: actual question
- assistant: previous response

This helps shape the model behavior more predictably.

## Thu: request/response flow

A real app handles:
- user input
- validation
- model call
- post-processing
- returning the result to the client

## Friday challenge

Write a tool that accepts a raw question and logs a structured request before sending it to a model.

## Saturday project

Build a lightweight LLM helper app in `projects/month7_llm_assistant/`.

## Did it stick? Repeat checklist

- I can explain what an LLM API is.
- I can explain why prompt structure matters.
- I can describe system and user messages.
- I can explain how an app passes a request through a remote API and returns the result.
