"""this is a code to generate the points/path for visualisations of randomwalk"""

from random import choice	#this will import the choice module to be used

class RandomWalk:
	"""a class to generate random walks"""

	def __init__(self, num_points=5000):
		"""initialising the attributes"""
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]

	def get_step(self):
		"""calculating the distance and direction of step"""
		direction = choice([-1, 1])
		distance = choice([0, 1, 2, 3, 4])
		step = direction * distance
		return step

	def fill_walk(self):
		"""appending the step to the already existing files"""
		#keep walking till the points are reached
		while len(self.x_values) < self.num_points:
			x_step = self.get_step()
			y_step = self.get_step()

			#if the step size is zero just ignore this and move on to the next iteration
			if x_step == 0 and y_step == 0:
				continue

			#calculate the new position
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			#append the new position to the list
			self.x_values.append(x)
			self.y_values.append(y)
