import time
import numpy as np

values = np.array([10, 20, 30, 40])
print("Add 5:", values + 5)
print("Multiply by 2:", values * 2)

# Compare a Python loop to NumPy vectorization.
loop_values = list(range(1_000_000))
start = time.perf_counter()
result = []
for value in loop_values:
    result.append(value * 2)
loop_time = time.perf_counter() - start

start = time.perf_counter()
array_result = np.array(loop_values) * 2
vector_time = time.perf_counter() - start

print(f"Loop time: {loop_time:.8f} seconds")
print(f"Vectorized time: {vector_time:.8f} seconds")
print("Array result sample:", array_result[:5])
