import common as c

Heads = "Heads"
Tails = "Tails"
weighted_sample_space = { Heads : 4, Tails : 1}


def is_heads_or_tails(outcome) : return outcome in weighted_sample_space
def is_neither(outcome): return not is_heads_or_tails(outcome)
def is_heads(outcome) : return outcome == Heads
def is_tails(outcome) : return outcome == Tails

event_conditons = [is_heads_or_tails, is_neither, is_heads, is_tails]
for event_condition in event_conditons:  
    probability = c.compute_probability(event_condition, weighted_sample_space)
    print(f'Probability of event arising from {event_condition.__name__} is  {probability}\n')