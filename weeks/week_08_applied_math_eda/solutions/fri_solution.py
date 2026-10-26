# Reference solution.
# Look only after you have tried.

import seaborn as sns

# Load the Titanic dataset

df = sns.load_dataset("titanic")

# Mean age by class
print("Mean age by class:")
print(df.groupby("pclass")["age"].mean())

# Correlation between fare and survival
print("\nFare-survival correlation:")
print(df[["fare", "survived"]].corr())

# Probability observation: probability of being female
print("\nProbability of female passenger:")
print((df["sex"] == "female").mean())
