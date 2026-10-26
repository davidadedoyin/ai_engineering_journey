from __future__ import annotations

from typing import Literal

import pandas as pd
import seaborn as sns
from fastapi import FastAPI
from pydantic import BaseModel, Field
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

app = FastAPI(title="Titanic Survival API")


class PassengerInput(BaseModel):
    pclass: int = Field(..., ge=1, le=3)
    sex: Literal["male", "female"]
    age: float = Field(..., ge=0)
    sibsp: int = Field(..., ge=0)
    parch: int = Field(..., ge=0)
    fare: float = Field(..., ge=0)
    embarked: Literal["C", "Q", "S", "c", "q", "s"]


def build_model():
    df = sns.load_dataset("titanic")
    df = df[["survived", "pclass", "sex", "age", "sibsp", "parch", "fare", "embarked"]].copy()
    df = df.dropna(subset=["survived", "pclass", "sex", "age", "fare", "embarked"]).copy()
    df["age"] = df["age"].fillna(df["age"].median())

    X = df[["pclass", "sex", "age", "sibsp", "parch", "fare", "embarked"]]
    y = df["survived"]

    numeric_features = ["pclass", "age", "sibsp", "parch", "fare"]
    categorical_features = ["sex", "embarked"]

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline([
                    ("imputer", SimpleImputer(strategy="median")),
                ]),
                numeric_features,
            ),
            (
                "cat",
                Pipeline([
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore")),
                ]),
                categorical_features,
            ),
        ]
    )

    model = LogisticRegression(max_iter=1000)
    pipeline = Pipeline([("preprocessor", preprocessor), ("model", model)])
    pipeline.fit(X, y)
    return pipeline


model = build_model()


@app.get("/")
def root():
    return {"message": "Titanic survival API is running."}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict_passenger(passenger: PassengerInput):
    payload = {
        "pclass": passenger.pclass,
        "sex": passenger.sex.lower(),
        "age": passenger.age,
        "sibsp": passenger.sibsp,
        "parch": passenger.parch,
        "fare": passenger.fare,
        "embarked": passenger.embarked.upper(),
    }

    frame = pd.DataFrame([payload])
    probability = model.predict_proba(frame)[0, 1]
    prediction = int(model.predict(frame)[0])

    return {
        "prediction": prediction,
        "survived": bool(prediction),
        "probability_survival": round(float(probability), 4),
    }
