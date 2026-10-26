# Week 12: Evaluation and FastAPI introduction

## Analogy

Think of a model like a student taking an exam. We do not just ask, "Did it get any right?" We also ask, "How often did it get things wrong, and what kinds of mistakes were made?"

## Mon: precision, recall, F1 and confusion matrix

These are classification metrics. They tell us how well the model is doing beyond simple accuracy.

Example:

- precision = among predicted positives, how many were actually positive?
- recall = among actual positives, how many did we find?
- F1 = a balance between precision and recall
- confusion matrix = table of true positives, false positives, true negatives and false negatives

## Tue: cross-validation

Cross-validation splits the data into multiple train/test folds so we do not trust one single split too much.

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]
model = LogisticRegression()
print(cross_val_score(model, X, y, cv=2))
```

## Wed: what is an API?

An API is a way for software to talk to other software.

Restaurant analogy:
- you order food
- the kitchen prepares it
- the waiter brings the food back

A web API works the same way: a client sends a request; a server processes it; the server returns a response.

## Thu: build the first FastAPI app

This is a simple example.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "hello"}
```

Then run it with:

```bash
uvicorn app:app --reload
```

## Friday challenge

Add a second endpoint that takes a number and returns even or odd.

## Saturday project

Wrap the Titanic classifier in FastAPI in `projects/month3_titanic_api/`: a `POST /predict` endpoint that returns a survival prediction and a probability.

## Did it stick? Repeat checklist

- I can explain precision, recall and F1 in plain language.
- I can explain why cross-validation helps.
- I can explain the restaurant-order analogy for an API.
- I can run a basic FastAPI app locally.
