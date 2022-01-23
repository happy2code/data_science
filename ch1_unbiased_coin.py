import common as c

Heads = "Heads"
Tails = "Tails"
sample_space = { Heads, Tails}


def is_heads_or_tails(outcome) : return outcome in sample_space
def is_neither(outcome): return not is_heads_or_tails(outcome)
def is_heads(outcome) : return outcome == Heads
def is_tails(outcome) : return outcome == Tails

event_conditons = [is_heads_or_tails, is_neither, is_heads, is_tails]
for event_condition in event_conditons:
    print(f'Event Condition: {event_condition.__name__}')
    event = c.matching_event(event_condition, sample_space)
    print(f'Event: {event}')
    probability = c.compute_probability(event_condition, sample_space)
    print(f'Probability : {probability}\n')
