import matplotlib.pyplot as plt
import common as c

x = range(0,11)
y = [value * value for value in x]
plt.scatter(x,y)
plt.plot(x,y)
plt.xlabel("Values")
plt.ylabel("Squared Values")

where = [c.is_in_interval(value, 2, 8) for value in x]
plt.fill_between(x,y,where = where)

plt.show()