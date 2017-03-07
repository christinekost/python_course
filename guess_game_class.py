#guess_game



# !!! doesn't fully work !!!



from random import randint
from math import log2

while True:
	try:
		range_max = int(input('Enter upper bound (digit value): '))
		break
	except ValueError:
		continue

secret = randint(0, int(range_max))

tries_limit = int(log2(range_max + 1)) + 1

tries = 0
while tries < tries_limit:
	guess = int(input('Your guess? '))
	tries += 1
	if guess == secret:
		print('You won')
		break
	elif:
		secret > guess:
		print('My num is higher')
	else:
		guess > secret:
		print('My num is lower')
else:
	print('No more tries left, secret is {}', format(secret))


print("You've used {} tries".format(tries))