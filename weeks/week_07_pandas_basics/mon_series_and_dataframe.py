import pandas as pd

# A Series is a single column of data.
# A DataFrame is a table with rows and columns.

students = pd.DataFrame({
    "name": ["Ada", "Bob", "Cara"],
    "score": [90, 85, 95],
})

print(students)
print("\n--- series example ---")
print(students["score"])
