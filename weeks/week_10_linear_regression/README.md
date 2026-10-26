# Week 10: Linear regression

## Analogy

Linear regression is like drawing the best straight line through a cloud of points. The line helps us predict a value for new data.

## Mon: what linear regression is

A linear regression model tries to learn a relationship between input features and a target value.

For example:
- input: house size
- target: house price

A simple model learns a line like:

price = a * size + b

The model chooses the values of `a` and `b` to make the predictions as close as possible to the real prices.

## Tue: fit the first model

```python
from sklearn.linear_model import LinearRegression

X = [[800], [1200], [1500], [2000]]
y = [150000, 220000, 300000, 380000]

model = LinearRegression()
model.fit(X, y)
print(model.predict([[1300]]))
```

This is the first real model of the roadmap.

## Wed: evaluation with MAE, MSE and R²

```python
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

predictions = model.predict(X)
print("MAE:", mean_absolute_error(y, predictions))
print("MSE:", mean_squared_error(y, predictions))
print("R²:", r2_score(y, predictions))
```

- MAE tells us the average size of the prediction error.
- MSE squares the errors, which punishes larger mistakes.
- R² tells us how much of the variation the model explains.

## Thu: compare different feature choices

If we add a second feature, such as number of bedrooms or distance to city, the model may improve.

Example:

```python
X = [[800, 2], [1200, 3], [1500, 4], [2000, 5]]
```

A model with more useful features often predicts better.

## Friday challenge

Train a small regression model on a new dataset and evaluate it end to end.

## Saturday project

Create a tiny “predict my own scenario” model, such as delivery time from distance and weight.

## Did it stick? Repeat checklist

- I can explain what linear regression does in plain English.
- I can fit a `LinearRegression` model.
- I can explain MAE, MSE and R² in simple terms.
- I can describe why adding a better feature can help.
