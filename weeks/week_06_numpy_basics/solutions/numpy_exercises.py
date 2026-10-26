# Reference solution.
# Look only after you have tried.

import numpy as np

# 1. Create an array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# 2. Get first and last values
print("First:", arr[0])
print("Last:", arr[-1])

# 3. Slice the middle
print("Middle:", arr[1:4])

# 4. Multiply by 2
print("Times 2:", arr * 2)

# 5. Shape of 2D array
matrix = np.array([[1, 2], [3, 4]])
print("Shape:", matrix.shape)

# 6. Reshape
print("Reshaped:", matrix.reshape(4, 1))

# 7. Sum
print("Sum:", arr.sum())

# 8. Mean
print("Mean:", arr.mean())

# 9. Max and min
print("Max:", arr.max())
print("Min:", arr.min())

# 10. Boolean mask
print("Even values:", arr[arr % 2 == 0])
