#date: 12/16/2020
#time: 1:04 AM

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
x_values = range(1, 5000)
y_values = [x**3 for x in x_values]
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

ax.set_title("Cube of numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of value", fontsize=14)
ax.tick_params(axis="both", labelsize=14)


plt.show()
