from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

model = LogisticRegression()
model.fit(X, y)

print("Prediction for 3.5:", model.predict([[3.5]]))
print("Probabilities for 3.5:", model.predict_proba([[3.5]]))
