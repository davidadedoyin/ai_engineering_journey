# Week 17: Prompt engineering and tool use

## Analogy

A model is a very capable assistant, but it needs good instructions. Prompt engineering is like giving a good brief to a very smart intern.

## Mon: prompting basics

A prompt is the instruction you send to a model. Good prompts clearly define:
- role
- task
- constraints
- expected format

```python
prompt = """
You are a helpful AI tutor.
Explain the idea of a confusion matrix in 3 bullet points.
Keep it simple and accurate.
"""
print(prompt)
```

## Tue: few-shot prompting

Few-shot prompting gives the model a few examples before asking the real question.

```python
examples = [
    ("Email: 'Why is my model performing badly?'", "Possible reasons include overfitting, data leakage, or a weak baseline."),
    ("Email: 'Can you explain feature importance?'", "Feature importance tells us which inputs matter most for the model."),
]
print(examples)
```

## Wed: tool use

A model can do more than generate text. It can also call tools, such as:
- a calculator
- a search function
- a database lookup
- a weather or translation API

Tool use makes the model more useful in real workflows.

## Thu: structured outputs

Structured outputs make the response easier for software to parse. Examples include JSON, lists, or specific schema fields.

```python
response = {
    "task": "classify_message",
    "label": "positive",
    "confidence": 0.92,
}
print(response)
```

## Friday challenge

Design a prompt that asks a model to classify a message and return JSON with `label`, `confidence`, and `reason`.

## Saturday project

Build a small tool-calling assistant in `projects/month8_agent_tool_use/`.

## Did it stick? Repeat checklist

- I can explain why prompt design matters.
- I can describe a few-shot example.
- I can explain how tool use extends a model beyond text generation.
- I can compare unstructured output with structured output.
