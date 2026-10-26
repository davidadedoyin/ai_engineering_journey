import numpy as np

# Mean, median, variance and standard deviation are basic statistics.
ages = np.array([20, 22, 28, 35, 40, 60])

print("Mean:", ages.mean())
print("Median:", np.median(ages))
print("Variance:", ages.var())
print("Std dev:", ages.std())
