from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X = [[800], [1200], [1500], [2000]]
y = [150000, 220000, 300000, 380000]

model = LinearRegression()
model.fit(X, y)
predictions = model.predict(X)

print("Predictions:", predictions)
print("MAE:", mean_absolute_error(y, predictions))
print("MSE:", mean_squared_error(y, predictions))
print("R²:", r2_score(y, predictions))
