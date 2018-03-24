import random

# Class to create a die with n sides. Gives you the method roll which returns a random side.
class Die:
	def __init__(self, num_sides):
		self.__num_sides = num_sides

	def roll(self):
		num = random.randint(1, self.__num_sides)
		return num
