a, b = 1, 1, 2

while len(fibs) < 10 ** 10:
	a, b, n = b, a + b, n + 1

print (len(str(b)))