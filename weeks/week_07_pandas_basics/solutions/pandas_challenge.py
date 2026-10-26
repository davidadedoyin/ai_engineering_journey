# Reference solution.
# Look only after you have tried.

import pandas as pd

# Build a tiny dataset

df = pd.DataFrame({
    "class": ["A", "A", "B", "B", "C"],
    "survived": [1, 0, 1, 1, 0],
    "fare": [10, 20, 8, 12, 15],
})

# Question 1: which class has the most rows?
print(df["class"].value_counts())

# Question 2: how many rows are missing?
print("Missing values:")
print(df.isnull().sum())

# Question 3: what is the survival rate by class?
print("Survival rate by class:")
print(df.groupby("class")["survived"].mean() * 100)
