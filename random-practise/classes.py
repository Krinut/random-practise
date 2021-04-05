#!/usr/bin/env python3

#date: 12/16/2020
#time: 11:38 AM

import sys	#in this program this is to use the exit command for quitting the program when I want to

class Restraunt:
	"""A class to define the restraunt and attributes related to it"""

	def __init__(self, restraunt_name, cuisine_type):
		self.name = restraunt_name	#this will define two variables calles name and cuisine. variable that are prefixed by self can be used by all the methods and instances of the class.
		self.cuisine = cuisine_type
		self.number_served = 0

	def describe_restraunt(self):
		print(f"printing through the class, Restraunt name: {self.name} Cuisine type: {self.cuisine}")

	def open_restraunt(self):
		print("The restraunt is now open")

	def set_number_served(self, customers):
		self.number_served = customers
		print(f"printing through the class, customer served = {self.number_served}")

	def increment_number_served(self, addition):
		self.number_served += addition

class IceCreamStand(Restraunt):
	"""This is a child class of Restraunt that inherits all the methods and attributes from the class. The init() method in this class accepts the parameters and then calls the init from Restraunt to initialise the attributes in it. We have also defined a new arrtibute flavours in this and a new method that displays the falvours."""

	def __init__(self, restraunt_name, cuisine_type):
		super().__init__(restraunt_name, cuisine_type)
		self.flavours = ["chocolate", "vanilla", "butterscotch", "cashew"]

	def display_flavours(self):
		for flavour in self.flavours:
			print(f"printing through the class, flavours: {flavour}")

restraunt = Restraunt("Taj 2", "Indian")
print(f"prinitng through instance, restraunt name: {restraunt.name} cuisine: {restraunt.cuisine}")
restraunt.describe_restraunt()
restraunt.open_restraunt()
#print(f"printing the number of customers without increment and default value: {restraunt.set_number_served()}")
print(f"printing the number of customers without increment: {restraunt.number_served}")
restraunt.increment_number_served(40)
print(f"printing the number of customers: {restraunt.number_served}")

icecream = IceCreamStand("McDonalds", "American Fast Food")
icecream.display_flavours()
