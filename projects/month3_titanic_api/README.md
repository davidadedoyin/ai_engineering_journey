# Titanic survival API

This project turns a simple Titanic survival classifier into a tiny FastAPI service.

## Goal

The app loads a real Titanic dataset, trains a logistic regression model, and exposes a `/predict` endpoint that returns whether a passenger is likely to survive.

## How to run

From the repo root:

```bash
cd ai-engineering-journey\.venv\Scripts
python -m uvicorn projects.month3_titanic_api.app:app --host 127.0.0.1 --port 8000 --reload
```

Or from inside the project directory:

```bash
cd ai-engineering-journey\projects\month3_titanic_api
python -m uvicorn app:app --host 127.0.0.1 --port 8000 --reload
```

## Example request

```json
{
  "pclass": 3,
  "sex": "male",
  "age": 28,
  "sibsp": 1,
  "parch": 0,
  "fare": 7.25,
  "embarked": "S"
}
```

## Response

```json
{
  "prediction": 0,
  "survived": false,
  "probability_survival": 0.2432
}
```

## Limitations

This is a learning project and not a production deployment. It keeps the model intentionally simple and does not include advanced validation, monitoring, or authentication.
