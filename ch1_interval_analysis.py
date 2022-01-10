import common as c
from collections import defaultdict
from itertools import product

def generate_coin_sample_space(no_of_flips = 10) :
    weighted_sample_space = defaultdict(int)
    for coin_flips in product(['Heads', 'Tails'],repeat=no_of_flips):
        heads_count = len([outcome for outcome in coin_flips if outcome == 'Heads'])
        weighted_sample_space[heads_count] += 1
    
    return weighted_sample_space

# Let’s find the probability of 20 fair coin flips not producing from 5 to 15 heads.
prob = c.compute_probability(lambda x : not c.is_in_interval(x, 5, 15), generate_coin_sample_space(20))
print(f"Probability of observing more than less than 5 heads/more than 15 heads is {prob}")