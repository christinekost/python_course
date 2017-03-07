list = [1, 3, 4, 2, 1, 3]

d = {}

for el in list:
	if el in d:
		d[el] += 1
	else:
		d[el] = 1

for word, count in d.items():
	if count > 1:
		print(word)