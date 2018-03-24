from die import Die

# Functions to roll the numbers 1-10 with a 6-sided die.
die6 = Die(6)

def roll10A():
	roll1 = die6.roll()
	offset = 5 if roll1 > 3 else 0

	while True:
		roll2 = die6.roll()
		if roll2 != 6:
			break

	return roll2 + offset

def roll10B():
	rolls = []
	for x in range(5):
		rolls.append(die6.roll())
	return reduce((lambda x, y: x + y), rolls) % 10 + 1
