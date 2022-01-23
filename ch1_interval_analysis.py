import common as c



# Let’s find the probability of 20 fair coin flips not producing from 5 to 15 heads.
prob = c.compute_probability(lambda x : not c.is_in_interval(x, 5, 15), c.generate_coin_sample_space(20))
print(f"Probability of observing more than less than 5 heads/more than 15 heads is {prob}")