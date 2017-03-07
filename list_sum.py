lst = [[1, 2, 3], [4, 5], [6], [7, 8, 9]]
total = 0
for inner in lst:
	total += sum(inner)
print(total)


# OR the other way
#list_sum = ([[1, 2, 3], [4, 5], [6], [7, 8, 9]])
#print(sum(sum(list_sum, [])))