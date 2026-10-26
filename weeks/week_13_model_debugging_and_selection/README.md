# Week 13: Model debugging and selection

## Analogy

A model is not just "trained" or "not trained." It also has to be judged fairly. A model that is too simple underfits the pattern. A model that is too complex memorizes noise and overfits.

## Mon: bias and variance

- Bias: error caused by simplistic assumptions.
- Variance: error caused by reacting too strongly to training-data noise.

A good model balances both.

```python
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = [[float(i)] for i in range(20)]
y = [x[0] + 0.1 * (x[0] ** 2) for x in X]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

for degree in [1, 2, 5, 10]:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    print(degree, model.score(X_train, y_train), model.score(X_test, y_test))
```

## Tue: train/validation/test split

We need different data for fitting and checking. Otherwise, the model can look better than it really is.

- Train: learn the pattern
- Validation: choose the hyperparameters
- Test: final honest evaluation

## Wed: data leakage

Leakage happens when information from the test set leaks into training. This makes the model look too good.

Examples:
- scaling before splitting the data
- using future data to predict past outcomes
- encoding target information into features

## Thu: debugging model problems

A useful checklist:

1. Check the shapes of the data.
2. Check for missing values.
3. Check whether your labels are balanced.
4. Compare train and validation performance.
5. Repeat on a simple baseline model.

If your model shows huge training performance but poor test performance, you likely have overfitting.

## Friday challenge

Train several small models on the same dataset and decide which one looks most reliable.

## Saturday project

Build a tiny sentiment API in `projects/month4_sentiment_api/`.

## Did it stick? Repeat checklist

- I can explain bias versus variance in plain English.
- I can describe why train/test splits matter.
- I can spot a data leakage problem.
- I can explain why a simple baseline is important in ML work.
