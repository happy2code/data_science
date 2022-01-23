from collections import defaultdict
from itertools import product

Heads = 'Heads'
Tails = 'Tails'
coin_values = [Heads, Tails]

def generate_coin_sample_space(no_of_flips = 10) :
    weighted_sample_space = defaultdict(int)
    for coin_flips in product(coin_values,repeat=no_of_flips):
        heads_count = len([outcome for outcome in coin_flips if outcome == Heads])
        weighted_sample_space[heads_count] += 1
    
    return weighted_sample_space

def matching_event(event_condition, sample_space):
    return set([outcome for outcome in sample_space if event_condition(outcome)])

def compute_probability(event_condition, generic_sample_space):
    event = matching_event(event_condition, generic_sample_space)
    if(type(generic_sample_space) == type(set())):
        return len(event)/len(generic_sample_space)

    event_size = sum(generic_sample_space[outcome] for outcome in event)
    return event_size / sum(generic_sample_space.values())

def is_in_interval(value, min, max):
    return min <= value <= max    