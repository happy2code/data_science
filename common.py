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