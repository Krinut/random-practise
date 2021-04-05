import matplotlib.pyplot as plt
import matplotlib.artist as art
from random_walk import RandomWalk

rw = RandomWalk()
rw.fill_walk()
counts = dict()

plt.style.use("classic")
fig, ax = plt.subplots()
point_numbers = list(range(rw.num_points))

#art.Artist.set_label("dance", point_numbers)

#print(point_numbers)

for (xvalue, yvalue) in rw.locations:
    counts[(xvalue,yvalue)] = counts.get((xvalue,yvalue),0) + 1

#print(counts)
frequency_list = list(counts.values())
print("length of counts is {} and frequency_list is {}".format(len(counts), len(frequency_list)))

#print(frequency_list)

ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15, label='path')

#setting the start and end point differently
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

#ax.get_legend().set_visible(True)
#leg.set_bbox_to_anchor((1.15,0.5))
ax.legend()
ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)

plt.show()
#print(rw.x_values, rw.y_values)
#print(rw.locations)