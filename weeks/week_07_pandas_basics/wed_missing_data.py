import pandas as pd

# Missing values are common in real datasets.
# We can either drop them or fill them.

df = pd.DataFrame({
    "name": ["Ada", "Bob", None],
    "score": [90, None, 85],
})

print("Original:")
print(df)
print("\nNull check:")
print(df.isnull())
print("\nDrop rows with missing values:")
print(df.dropna())
print("\nFill missing scores with the mean:")
filled = df.copy()
filled["score"] = filled["score"].fillna(filled["score"].mean())
print(filled)
