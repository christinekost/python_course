lst = [1, 2, 3, 2, 2, 2, 4]


d = {}


for el in lst:
	if el in d:
		d[el] += d.setdefault(el, 0) + 1


for el, count in d.items():
	if count > 1:
		print(el)

		