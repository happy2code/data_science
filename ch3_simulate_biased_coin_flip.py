import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict


np.random.seed(0)
# binomial returns a numpy array rather than a standard python list. It offers optimizations and easy functions
head_count = np.random.binomial(2000, 0.7, 500)

# this division of head_count, returns a numpy array that has each element divided by 1000
frequencies = head_count/2000 

min_frequency = frequencies.min()
max_frequency = frequencies.max()

print(f"Minimum frequency observed: {min_frequency}")
print(f"Maximum frequency observed: {max_frequency}")
print(f"Difference across frequency range: {max_frequency - min_frequency}")


plt.hist(frequencies, bins='auto', edgecolor='black')
plt.xlabel('Frequency')
plt.ylabel('Count')
plt.show()
