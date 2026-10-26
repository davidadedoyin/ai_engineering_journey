from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Compare a model using only size vs a model using size + rooms.
X_simple = [[800], [1200], [1500], [2000]]
X_better = [[800, 2], [1200, 3], [1500, 4], [2000, 5]]
y = [150000, 220000, 300000, 380000]

simple_model = LinearRegression().fit(X_simple, y)
better_model = LinearRegression().fit(X_better, y)

print("Simple model R²:", r2_score(y, simple_model.predict(X_simple)))
print("Better model R²:", r2_score(y, better_model.predict(X_better)))
