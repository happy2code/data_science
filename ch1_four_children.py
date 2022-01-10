# Suppose a family has four children. What is the probability that exactly two of the children are boys? 
# We’ll assume that each child is equally likely to be either a boy or a girl.

from itertools import product
import common as c

possible_children = ['Boy', 'Girl']
sample_space = set(product(possible_children, repeat=4))

def has_two_boys(outcome) : return len([child for child in outcome if child=='Boy']) == 2
prob = c.compute_probability(has_two_boys, sample_space)

print(f'Probability of 2 boys is {prob}')