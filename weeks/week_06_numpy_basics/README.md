# Week 06: NumPy basics

## Analogy

A NumPy array is like a super-fast box of numbers. Normal Python lists can store numbers too, but NumPy lets us do math across the whole box at once. This is called vectorization.

## Mon: arrays

```python
import numpy as np

numbers = np.array([10, 20, 30, 40])
print(numbers)
print(numbers.dtype)
print(numbers.shape)
```

### Line-by-line walkthrough

- `import numpy as np` loads the NumPy library and gives it the short name `np`.
- `np.array([...])` creates a NumPy array from a list of numbers.
- `print(numbers)` displays the array.
- `numbers.dtype` tells us the data type, such as `int64`.
- `numbers.shape` tells us the shape of the array. A 1D array with 4 values has shape `(4,)`.

### Real output

```text
[10 20 30 40]
int64
(4,)
```

## Tue: indexing and slicing

```python
import numpy as np

values = np.array([10, 20, 30, 40, 50])
print("First item:", values[0])
print("Middle slice:", values[1:4])
print("Reverse:", values[::-1])
```

### Line-by-line walkthrough

- `values[0]` picks the first item.
- `values[1:4]` takes items from index 1 up to index 3.
- `values[::-1]` reverses the array. The `::-1` part means "step backwards by 1".

### Real output

```text
First item: 10
Middle slice: [20 30 40]
Reverse: [50 40 30 20 10]
```

## Wed: vectorized math

```python
import time
import numpy as np

values = np.array([10, 20, 30, 40])
print("Add 5:", values + 5)
print("Multiply by 2:", values * 2)

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
```

### Line-by-line walkthrough

- `values + 5` adds 5 to every value in the array.
- `values * 2` multiplies every value by 2.
- The loop version does the work one number at a time.
- The NumPy version does the math for the full array in one step.
- This is often much faster, which is why vectorization matters.

### Real output

```text
Add 5: [15 25 35 45]
Multiply by 2: [20 40 60 80]
Loop time: 0.59981470 seconds
Vectorized time: 0.09848600 seconds
Array result sample: [0 2 4 6 8]
```

## Thu: 2D arrays

```python
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
])

print("Shape:", matrix.shape)
print("Row 0:", matrix[0])
print("Column 1:", matrix[:, 1])
print("Last element:", matrix[1, 2])
```

### Line-by-line walkthrough

- `matrix.shape` shows the array dimensions.
- `matrix[0]` picks the first row.
- `matrix[:, 1]` picks every row in column 1.
- `matrix[1, 2]` picks a single value at row 1, column 2.

### Real output

```text
Shape: (2, 3)
Row 0: [1 2 3]
Column 1: [2 5]
Last element: 6
```

## Friday challenge

The Friday challenge is to write 10 NumPy exercises without notes and then explain the meaning of `shape`, `dtype`, slicing and vectorization.

## Saturday project: retention test

We redo the ideas from Monday to Thursday from memory. The blank notebook is in `retention_test.ipynb`, and the answer key is in `solutions/retention_answers.py`.

## Did it stick? Repeat checklist

- I can explain what a NumPy array is.
- I can index and slice arrays.
- I can see why vectorized math is faster than a Python loop.
- I can read a 2D array by row, column and shape.
