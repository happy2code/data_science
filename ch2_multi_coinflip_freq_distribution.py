import common as c
import matplotlib.pyplot as plt 

sample_space_10_flips = c.generate_coin_sample_space(10)
x_10_flips = list(sample_space_10_flips.keys())
x_10_frequencies = [head_count/10 for head_count in x_10_flips]

y_10_flips = [sample_space_10_flips[key] for key in x_10_flips]
prob_x_10_flips = [value / sum(sample_space_10_flips.values()) for value in y_10_flips]
relative_likelihood_10 = [10 * prob for prob in prob_x_10_flips]

sample_space_20_flips = c.generate_coin_sample_space(20)

x_20_flips = list(sample_space_20_flips.keys())
x_20_frequencies = [head_count/20 for head_count in x_20_flips]

y_20_flips = [sample_space_20_flips[key] for key in x_20_flips]
prob_x_20_flips = [value / sum(sample_space_20_flips.values()) for value in y_20_flips]
relative_likelihood_20 = [20 * prob for prob in prob_x_20_flips]

plt.plot(x_10_frequencies, relative_likelihood_10, label='A: 10 coin-flips')
plt.plot(x_20_frequencies, relative_likelihood_20, color='black', linestyle='--', label='B: 20 coin-flips')
plt.legend()

where_10 = [not c.is_in_interval(value, .3,.7) for value in x_10_frequencies]
plt.fill_between(x_10_frequencies, relative_likelihood_10, where=where_10)

where_20 = [not c.is_in_interval(value,.3,.7) for value in x_20_frequencies]
plt.fill_between(x_20_frequencies,relative_likelihood_20, where=where_20)

plt.xlabel('Head-Frequency')
plt.ylabel('Relative Likelihood')

plt.show()