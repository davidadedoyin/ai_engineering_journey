# Week 08: Applied math and the Month 2 capstone

## Analogy

A vector is like a list of measurements, such as a student's scores across different subjects. Statistics help us describe that list with a few useful numbers.

## Mon: vectors and matrices

```python
import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])
print(vector_a + vector_b)
print(np.dot(vector_a, vector_b))
```

### Line-by-line walkthrough

- `np.array([...])` creates vectors.
- `vector_a + vector_b` adds them element by element.
- `np.dot(...)` computes a dot product, which is a common ML operation.

### Real output

```text
A: [1 2 3]
B: [4 5 6]
A + B: [5 7 9]
Dot product: 32
```

## Tue: mean, median, variance and standard deviation

```python
import numpy as np

ages = np.array([20, 22, 28, 35, 40, 60])
print("Mean:", ages.mean())
print("Median:", np.median(ages))
print("Variance:", ages.var())
print("Std dev:", ages.std())
```

### Real output

```text
Mean: 34.166666666666664
Median: 31.5
Variance: 198.47222222222223
Std dev: 14.088
```

## Wed: correlation

```python
import pandas as pd

df = pd.DataFrame({
    "hours_studied": [1, 2, 3, 4, 5],
    "score": [50, 60, 70, 80, 90],
})

print(df.corr())
```

### Line-by-line walkthrough

- `df.corr()` calculates the pairwise correlation between columns.
- A high positive value means values move together.
- This does not prove one thing caused the other.

### Real output

```text
             hours_studied  score
hours_studied           1.0    1.0
score                   1.0    1.0
```

## Thu: probability and randomness

```python
import numpy as np

flips = np.random.default_rng(0).choice(["H", "T"], size=20)
print(flips)
print("Heads count:", np.count_nonzero(flips == "H"))
```

### Line-by-line walkthrough

- `choice([...], size=20)` makes 20 random flips.
- `np.count_nonzero(...)` counts how many were heads.
- This is a tiny example of probability in action.

## ADDITION: Matplotlib primer

Charts are a simple way to explain data quickly.

- histogram: shows the distribution of one numeric variable
- bar chart: compares groups
- scatter plot: looks for relationships between two variables
- titles and axis labels: make the visual readable

See `matplotlib_primer.py` for a minimal example and generated chart.

## Friday challenge

Compute and explain in plain English:
- mean age by class
- fare-survival correlation
- one probability observation

## Saturday project: Month 2 capstone

The Titanic EDA project lives in `projects/month2_titanic_eda/`. It includes a cleaned EDA script and an exported chart. This is the first polished portfolio notebook-style project in the repo.

## Sun: rest + reflection

See `reflection.md` for the weekly reflection prompts.

## Did it stick? Repeat checklist

- I can explain a vector in plain English.
- I can calculate and interpret mean, median and standard deviation.
- I can explain what correlation means and does not mean.
- I can describe a probability example without jargon.
