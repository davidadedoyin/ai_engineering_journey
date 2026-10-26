import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# A tiny primer for plotting by hand.
# Histogram: distribution of one numeric variable.
# Bar chart: compare groups.
# Scatter: relationship between two variables.

values = [10, 12, 20, 18, 30, 28, 40, 35]

plt.figure(figsize=(8, 4))
plt.hist(values, bins=6)
plt.title("Histogram example")
plt.xlabel("Value")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("histogram_example.png")
print("Saved histogram_example.png")
