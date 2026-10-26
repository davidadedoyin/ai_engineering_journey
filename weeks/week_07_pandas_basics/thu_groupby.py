import pandas as pd

# Groupby lets us summarize by a category.

df = pd.DataFrame({
    "class": ["A", "A", "B", "B"],
    "survived": [1, 0, 1, 1],
})

summary = df.groupby("class")["survived"].mean()
print(summary)
print("\nPercent survived by class:")
print(summary * 100)
