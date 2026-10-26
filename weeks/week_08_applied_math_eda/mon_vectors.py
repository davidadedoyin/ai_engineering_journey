import numpy as np

# A vector is a list of numbers.
# We can do math with the whole vector at once.

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

print("A:", vector_a)
print("B:", vector_b)
print("A + B:", vector_a + vector_b)
print("Dot product:", np.dot(vector_a, vector_b))
