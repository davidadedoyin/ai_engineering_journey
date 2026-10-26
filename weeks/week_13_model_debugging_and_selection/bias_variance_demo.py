from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

# Synthetic data with a curved pattern.
X = [[float(i)] for i in range(30)]
y = [x[0] ** 2 / 5 + 2 * x[0] + 1 for x in X]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

for degree in [1, 2, 4, 8]:
    model = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    model.fit(X_train, y_train)
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    print(f"degree={degree} train_r2={train_score:.3f} test_r2={test_score:.3f}")
