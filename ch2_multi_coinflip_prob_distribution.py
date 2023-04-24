import common as c
import matplotlib.pyplot as plt 

sample_space_10_flips = c.generate_coin_sample_space(10)
x_10_flips = list(sample_space_10_flips.keys())
y_10_flips = [sample_space_10_flips[key] for key in x_10_flips]
prob_x_10_flips = [value / sum(sample_space_10_flips.values()) for value in y_10_flips]

sample_space_20_flips = c.generate_coin_sample_space(20)
x_20_flips = list(sample_space_20_flips.keys())
y_20_flips = [sample_space_20_flips[key] for key in x_20_flips]
prob_x_20_flips = [value / sum(sample_space_20_flips.values()) for value in y_20_flips]

plt.plot(x_10_flips, prob_x_10_flips, label='A: 10 coin-flips')
plt.plot(x_20_flips, prob_x_20_flips, color='black', linestyle='--', label='B: 20 coin-flips')
plt.legend()

where_10 = [not c.is_in_interval(value, 3,7) for value in x_10_flips]
plt.fill_between(x_10_flips, prob_x_10_flips, where=where_10)

where_20 = [not c.is_in_interval(value,5,15) for value in x_20_flips]
plt.fill_between(x_20_flips,prob_x_20_flips, where=where_20)

plt.xlabel('Head-count')
plt.ylabel('Probability')

plt.show()