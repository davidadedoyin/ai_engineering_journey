from sklearn.model_selection import train_test_split

# We split data into training and testing sets.
# The model learns from the training set, then is checked on test data.

X = [1, 2, 3, 4, 5, 6, 7, 8]
y = [2, 4, 6, 8, 10, 12, 14, 16]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

print("X_train:", X_train)
print("X_test:", X_test)
print("y_train:", y_train)
print("y_test:", y_test)
