"""A small reproducible example of preprocessing inside an ML pipeline."""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main() -> None:
    rows = [
        (1, "basic", 0), (2, "basic", 0), (3, "basic", 0), (4, "basic", 0),
        (5, "basic", 0), (6, "basic", 0), (7, "basic", 0), (8, "basic", 0),
        (2, "pro", 0), (3, "pro", 0), (4, "pro", 0), (5, "pro", 0),
        (6, "pro", 1), (7, "pro", 1), (8, "pro", 1), (9, "pro", 1),
        (10, "pro", 1), (11, "pro", 1), (12, "pro", 1), (13, "pro", 1),
    ]
    frame = pd.DataFrame(rows, columns=["weekly_requests", "plan", "needs_review"])
    features = frame[["weekly_requests", "plan"]]
    target = frame["needs_review"]
    x_train, x_test, y_train, y_test = train_test_split(
        features,
        target,
        test_size=0.25,
        random_state=21,
        stratify=target,
    )

    numeric = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler()),
        ]
    )
    categorical = Pipeline(
        steps=[
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("encoder", OneHotEncoder(handle_unknown="ignore")),
        ]
    )
    preprocessing = ColumnTransformer(
        transformers=[
            ("numeric", numeric, ["weekly_requests"]),
            ("categorical", categorical, ["plan"]),
        ]
    )
    model = Pipeline(
        steps=[
            ("preprocessing", preprocessing),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )
    model.fit(x_train, y_train)
    predictions = model.predict(x_test)
    accuracy = accuracy_score(y_test, predictions)

    unseen_category = pd.DataFrame(
        [{"weekly_requests": 6, "plan": "enterprise"}]
    )
    unseen_prediction = int(model.predict(unseen_category)[0])

    print(f"Held-out accuracy: {accuracy:.2f}")
    print(f"Prediction for unseen plan category: {unseen_prediction}")
    print("Synthetic data is for demonstration only; this score is not a production estimate.")


if __name__ == "__main__":
    main()
