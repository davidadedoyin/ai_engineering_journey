# Sentiment API

This project builds a minimal sentiment classifier using a small text dataset and a scikit-learn pipeline.

## Goal

The service takes a message and returns a sentiment label such as `positive` or `negative` along with a confidence score.

## How to run

```bash
cd ai-engineering-journey
.venv\Scripts\python.exe -m uvicorn projects.month4_sentiment_api.app:app --host 127.0.0.1 --port 8002 --reload
```

## Example request

```json
{
  "text": "I love this product and it works really well."
}
```

## Example response

```json
{
  "label": "positive",
  "score": 0.92
}
```

## Limitations

This is a beginner-friendly teaching app. It uses a compact example dataset and is intentionally simple. It is not a production NLP service.
