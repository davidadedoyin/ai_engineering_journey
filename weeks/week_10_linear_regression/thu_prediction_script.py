from sklearn.linear_model import LinearRegression

# Predict delivery time from distance and weight.
X = [[10, 2], [20, 4], [30, 6], [40, 8]]
y = [6, 12, 18, 24]

model = LinearRegression()
model.fit(X, y)

new_case = [[25, 5]]
print("Predicted delivery time:", model.predict(new_case)[0])
