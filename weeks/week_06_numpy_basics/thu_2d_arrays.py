import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print("Shape:", matrix.shape)
print("Row 0:", matrix[0])
print("Column 1:", matrix[:, 1])
print("Last element:", matrix[1, 2])
