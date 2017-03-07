lst = [[1, 2, 3], 4, 5, 6, [7, 8, 9]]
total = 0
# for el in lst:
# 	try:
# 		total += el
# 	except TypeError:
# 		total += sum(el)

for el in lst:
	if type(el) is int:
		total += el
	else:
		total += sum(el)
