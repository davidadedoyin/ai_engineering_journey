from sklearn.linear_model import LinearRegression

# House size -> house price
# This is a tiny regression dataset.
X = [[800], [1200], [1500], [2000]]
y = [150000, 220000, 300000, 380000]

model = LinearRegression()
model.fit(X, y)

print("Model coefficients:", model.coef_)
print("Model intercept:", model.intercept_)
print("Prediction for 1300 sq ft:", model.predict([[1300]])[0])
