# Week 07: Pandas basics

## Analogy

A pandas DataFrame is like a spreadsheet in Python. It lets you organize rows and columns, clean data, and answer questions with code.

## Mon: Series and DataFrame

```python
import pandas as pd

students = pd.DataFrame({
    "name": ["Ada", "Bob", "Cara"],
    "score": [90, 85, 95],
})

print(students)
print(students["score"])
```

### Line-by-line walkthrough

- `pd.DataFrame(...)` creates a table.
- Each column is a Series.
- `students["score"]` selects one column and shows all its values.

### Real output

```text
   name  score
0  Ada     90
1  Bob     85
2  Cara     95
0    90
1    85
2    95
Name: score, dtype: int64
```

## Tue: selecting and filtering

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Ada", "Bob", "Cara", "Drew"],
    "score": [90, 70, 95, 60],
})

print(df["name"])
print(df[df["score"] >= 80])
```

### Line-by-line walkthrough

- `df["name"]` selects a column.
- `df["score"] >= 80` creates a True/False mask.
- Using that mask keeps only rows that pass the test.

### Real output

```text
0    Ada
1    Bob
2    Cara
3    Drew
Name: name, dtype: object

   name  score
0  Ada     90
2  Cara     95
```

## Wed: missing data

```python
import pandas as pd

df = pd.DataFrame({
    "name": ["Ada", "Bob", None],
    "score": [90, None, 85],
})

print(df.isnull())
print(df.dropna())
filled = df.copy()
filled["score"] = filled["score"].fillna(filled["score"].mean())
print(filled)
```

### Line-by-line walkthrough

- `isnull()` marks missing values as True.
- `dropna()` removes rows with missing data.
- `fillna(...)` replaces missing values with something else, like the mean.

### Real output

```text
     name  score
0  False  False
1  False   True
2   True  False

   name  score
0  Ada   90.0
2  Cara   85.0

   name  score
0  Ada   90.0
1  Bob   87.5
2  Cara   85.0
```

## Thu: grouping

```python
import pandas as pd

df = pd.DataFrame({
    "class": ["A", "A", "B", "B"],
    "survived": [1, 0, 1, 1],
})

summary = df.groupby("class")["survived"].mean()
print(summary * 100)
```

### Line-by-line walkthrough

- `groupby("class")` splits the data by category.
- `mean()` calculates the average survival rate per class.
- Multiplying by 100 turns the value into a percentage.

### Real output

```text
class
A    50.0
B    100.0
Name: survived, dtype: float64
```

## Friday challenge

Use a new dataset, clean it, and answer three questions with pandas, using selection, missing-data handling and `groupby()`.

## Saturday project

The full Titanic cleaning pass and documentation happen in the Month 2 capstone project. This week gives the core pandas tools needed for that work.

## Did it stick? Repeat checklist

- I can explain a DataFrame and a Series.
- I can select columns and filter rows.
- I can identify missing values and handle them.
- I can use `groupby()` to summarize categories.
