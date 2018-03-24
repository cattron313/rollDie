from roll10 import roll10A, roll10B
from die import Die

die10 = Die(10)
experiment = [die10.roll, roll10A, roll10B]
results = []

# This is a sanity check to see if 10000 rolls produce something
# that seems close to uniform distribution.
for fn in experiment:
	result = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0}
	results.append(result)
	for x in range(10000):
		roll = fn()
		result[str(roll)] += 1
	print str(result)
