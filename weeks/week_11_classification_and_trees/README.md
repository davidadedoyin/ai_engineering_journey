# Week 11: Classification, logistic regression and decision trees

## Analogy

A classifier is like a yes/no decision tree. It looks at features and decides which bucket a case belongs to.

## Mon: classification recap

Classification is the task of predicting a label from input data.

Examples:
- will this email be spam or not?
- will this passenger survive or not?

The model outputs a class, such as `0` or `1`.

## Tue: logistic regression

Logistic regression is a classification model. It predicts a probability, then turns that probability into a class.

```python
from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

model = LogisticRegression()
model.fit(X, y)
print(model.predict([[3.5]]))
print(model.predict_proba([[3.5]]))
```

## Wed: decision trees

A decision tree is like a flowchart of yes/no questions. It keeps asking questions until it decides a class.

```python
from sklearn.tree import DecisionTreeClassifier, export_text

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]
model = DecisionTreeClassifier(max_depth=2)
model.fit(X, y)
print(model.tree_.feature)
print(export_text(model, feature_names=["feature"]))
```

## Thu: compare logistic regression vs decision tree

Both models can classify the same data, but they work differently.

- Logistic regression learns a probability curve.
- A decision tree keeps splitting data into smaller decision regions.

## Friday challenge

Train both models on a new dataset and decide which one works better and why.

## Saturday project

Tune `max_depth` on a tree and watch overfitting happen as depth increases.

## Did it stick? Repeat checklist

- I can explain classification in plain English.
- I can explain how logistic regression outputs a probability.
- I can describe a decision tree as a series of yes/no questions.
- I can compare two classifiers and explain which one fits the data better.
