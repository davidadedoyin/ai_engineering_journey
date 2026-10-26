from sklearn.tree import DecisionTreeClassifier, export_text

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 0, 1, 1]

model = DecisionTreeClassifier(max_depth=2)
model.fit(X, y)

print("Tree feature values:", model.tree_.feature)
print(export_text(model, feature_names=["feature"]))
