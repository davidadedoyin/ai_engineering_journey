from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]

model = LogisticRegression()
print(cross_val_score(model, X, y, cv=2))
