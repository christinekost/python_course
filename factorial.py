#def factorial(6):
#	return reduce(lambda x,y:x*y, [1]+range(1,6+1))


def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

print(factorial(6))




def avg(*x):
	return sum(x)/len(x)
	