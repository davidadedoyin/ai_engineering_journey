from __future__ import annotations

from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

app = FastAPI(title="Sentiment API")

training_texts = [
    "I love this product", "this is excellent", "amazing quality", "so happy with it",
    "very bad experience", "terrible service", "awful quality", "hated it",
    "great value for money", "this is wonderful", "super useful and helpful",
    "I feel disappointed and frustrated", "really nice and friendly", "excellent support",
    "not worth the money", "poor design", "perfect for my needs", "I am delighted",
    "very disappointed", "the product was a disaster"
]
training_labels = [
    "positive", "positive", "positive", "positive",
    "negative", "negative", "negative", "negative",
    "positive", "positive", "positive",
    "negative", "positive", "positive",
    "negative", "negative", "positive", "positive",
    "negative", "negative"
]

model = Pipeline([
    ("vectorizer", CountVectorizer()),
    ("classifier", LogisticRegression(max_iter=1000))
])
model.fit(training_texts, training_labels)


class SentimentRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "Sentiment API is running."}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: SentimentRequest):
    probabilities = model.predict_proba([request.text])[0]
    label_index = int(probabilities.argmax())
    label = model.classes_[label_index]
    score = float(probabilities[label_index])
    return {
        "label": label,
        "score": round(score, 4),
    }
