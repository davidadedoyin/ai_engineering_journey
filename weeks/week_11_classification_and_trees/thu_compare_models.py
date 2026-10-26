from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]

logreg = LogisticRegression()
logreg.fit(X, y)

clf = DecisionTreeClassifier(max_depth=3)
clf.fit(X, y)

print("Logistic prediction:", logreg.predict([[2.5], [6.5]]))
print("Tree prediction:", clf.predict([[2.5], [6.5]]))
print("Logistic accuracy:", accuracy_score(y, logreg.predict(X)))
print("Tree accuracy:", accuracy_score(y, clf.predict(X)))
