# Suppose we’re shown a fair six-sided die whose faces are numbered from 1 to 6. The die is rolled six times.
# What is the probability that these six die rolls add up to 21?
from itertools import product
from collections import defaultdict

import common as c

possible_rolls = list(range(1,7))
sample_space = set(product(possible_rolls, repeat=6))

def sum_upto_21(outcome) :  return sum(outcome) == 21
prob1 = c.compute_probability(sum_upto_21, sample_space)
print(f'Probability of values adding up to 21 is {prob1}')


# the following is more effective because we calculate the sum in each roll and cahe that as the sample_space. The first method
# however calculates the sum everytime we call the event_condition

weighted_sample_space = defaultdict(int)
for outcome in sample_space:
    weighted_sample_space[sum(outcome)] += 1

prob2 = c.compute_probability(lambda x : x == 21, weighted_sample_space)
print(f'Probability of values adding up to 21 is {prob2}')

assert(prob1 == prob2)