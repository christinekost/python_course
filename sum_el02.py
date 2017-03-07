lst = [[1, 2, [3, 4], 5], [6], [7, [8], 9], 10]
def msum(lst):
	total = 0
	for el in lst:
		try:
			total += el
		except TypeError:
			total += msum(el)
	return total
print(msum(lst))