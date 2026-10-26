# Reference solution.
# Look only after you have tried.

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X = [[1], [2], [3], [4], [5]]
y = [2, 4, 6, 8, 10]

model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)

print("Predictions:", predictions)
print("MAE:", mean_absolute_error(y, predictions))
print("MSE:", mean_squared_error(y, predictions))
print("R²:", r2_score(y, predictions))
