a, b = 1, 1

while b < 10**7:
	a, b = b, a + b
print(b)


a, b = 1, 1
while len(str(b)) < 1000:
	a, b = b, a + b
print(b)


a, b = 1, 1
while b < 10**999:
	a, b = b, a + b
print(b)