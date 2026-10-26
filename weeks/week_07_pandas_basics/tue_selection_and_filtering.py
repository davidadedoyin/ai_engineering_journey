import pandas as pd

# Filtering means keeping only rows that match a rule.

df = pd.DataFrame({
    "name": ["Ada", "Bob", "Cara", "Drew"],
    "score": [90, 70, 95, 60],
})

print("All names:")
print(df["name"])

print("\nHigh scorers:")
print(df[df["score"] >= 80])
