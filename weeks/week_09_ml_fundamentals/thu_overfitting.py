import numpy as np

# This is a toy demonstration of overfitting.
# A very flexible model can memorize noise instead of the real pattern.

x = np.array([1, 2, 3, 4, 5, 6])
y = np.array([2, 4, 6, 8, 10, 12])

# A simple straight-line pattern is the real relationship.
# A very flexible fit would chase every small wiggle.
print("Real pattern example:")
print("x:", x)
print("y:", y)
print("The relationship is roughly y = 2x")
