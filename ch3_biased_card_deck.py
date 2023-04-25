import numpy as np
import common as c
import matplotlib.pyplot as plt

total_cards = 52
# since the card deck is biased, we need to have a random number of red cards. 
red_card_count = np.random.randint(0, total_cards + 1)
black_card_count = total_cards - red_card_count

# with the number obtained above, let us create our weighted sample space and compute the probability
weighted_sample_space = {'red_card': red_card_count, 'black_card':black_card_count}
probability_red = c.compute_probability( lambda x : x == 'red_card', weighted_sample_space)
assert probability_red == red_card_count/total_cards

# simulate the lookup of one card, by doing it 50000 times and repeat it 100000 times
red_card_count_array = np.random.binomial(50000,probability_red, 100000)
freqency_array = red_card_count_array/50000

likelihoods, bin_edges, patches = plt.hist(freqency_array, density=True, bins='auto')
bin_width = bin_edges[1] - bin_edges[0]
start_index, end_index = c.compute_high_confidence_interval(likelihoods, bin_width)

print(f"The probability should lie between {freqency_array[start_index]} and {freqency_array[end_index]}")
range_start = round(freqency_array[start_index] * total_cards)
range_end = round(freqency_array[end_index] * total_cards)
print(f"Number of red cards(from experiment) is between {range_start} and {range_end}")
print(f"Number of actual red cards is {red_card_count}")

