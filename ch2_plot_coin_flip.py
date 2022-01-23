import common as c
import matplotlib.pyplot as plt 

sample_space_10 = c.generate_coin_sample_space(10)
sample_space_10_size = sum(sample_space_10.values())
head_counts = list(sample_space_10.keys())
probability_of_x_heads = [sample_space_10[key]/sample_space_10_size for key in head_counts]
assert sum(probability_of_x_heads) == 1
plt.scatter(head_counts, probability_of_x_heads)
plt.plot(head_counts, probability_of_x_heads)
where = [not c.is_in_interval(value, 3, 7) for value in head_counts]
plt.fill_between(head_counts, probability_of_x_heads, where = where)
plt.xlabel("Count of heads")
plt.ylabel("Probability x heads")
plt.show()
