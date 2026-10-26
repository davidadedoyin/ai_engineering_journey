import numpy as np

# Probability means how often something happens.
# A fair coin has a 50% chance of heads and 50% chance of tails.

flips = np.random.default_rng(0).choice(["H", "T"], size=20)
print(flips)
print("Heads count:", np.count_nonzero(flips == "H"))
