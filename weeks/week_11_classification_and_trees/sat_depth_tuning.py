from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[1], [2], [3], [4], [5], [6], [7], [8]]
y = [0, 0, 0, 0, 1, 1, 1, 1]

for depth in [1, 2, 3, 4]:
    model = DecisionTreeClassifier(max_depth=depth)
    model.fit(X, y)
    print(f"Depth {depth}: accuracy {accuracy_score(y, model.predict(X))}")
