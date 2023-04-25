import numpy as np
import matplotlib.pyplot as plt

def frequency_heads(coin_flip_sequence):
    total_heads = sum(coin_flip_sequence)
    return total_heads/len(coin_flip_sequence)

np.random.seed(0)
coin_flips = []
y_frequencies = []
for _ in range(1000):
    coin_flips.append(list(np.random.binomial(1,2)))
    y_frequencies.append(frequency_heads(coin_flips))

plt.plot(list(range(1000)), y_frequencies)
plt.axhline(.5, color='red')
plt.xlabel('Number of coin flips')
plt.ylabel('Head Frequency')
plt.show()