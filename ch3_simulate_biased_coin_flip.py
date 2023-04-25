import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

def compute_high_confidence_interval(lhoods, width):
    peak_index = lhoods.argmax()
    area = lhoods[peak_index] * width
    start_index, end_index = peak_index, peak_index + 1
    while area < 0.95:
        if start_index > 0:
            start_index -= 1
        if end_index < lhoods.size - 1:
            end_index += 1

        area = lhoods[start_index : end_index + 1].sum() * width

    return start_index, end_index

trials = 50000
experiment_size = 100000
np.random.seed(0)
# binomial returns a numpy array rather than a standard python list. It offers optimizations and easy functions
head_count = np.random.binomial(trials, 0.7, experiment_size)

# this division of head_count, returns a numpy array that has each element divided by trials
frequencies = head_count/trials 

min_frequency = frequencies.min()
max_frequency = frequencies.max()

print(f"Minimum frequency observed: {min_frequency}")
print(f"Maximum frequency observed: {max_frequency}")
print(f"Difference across frequency range: {max_frequency - min_frequency}")

likelihoods, bin_edges, patches   = plt.hist(frequencies, bins='auto', edgecolor='black', density=True)
bin_width = bin_edges[1] - bin_edges[0]

print(likelihoods.sum() * bin_width)

start_index, end_index = compute_high_confidence_interval(likelihoods, bin_width)

for i in range(start_index, end_index):
    patches[i].set_facecolor('yellow')

plt.xlabel('Binned Frequency')
plt.ylabel('Relative Likelihood')
plt.show()