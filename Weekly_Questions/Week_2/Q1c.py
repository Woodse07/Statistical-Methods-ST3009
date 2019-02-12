from random import randint

count = 0
rolls = 1000000
for i in range(rolls):
	roll1 = randint(1,6)
	roll2 = randint(1,6)
	roll3 = randint(1,6)
	if roll1 is 2 or roll2 is 2 or roll3 is 2:
		count += 1


probability = count / float(rolls)
print(probability)
