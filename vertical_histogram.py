# vertical histogram



# !!!! doesn't really work yet !!!!!




data = [1, 3, 7, 4, 7, 3, 2]

max(data) = 12
lst = []
new_lst = []

big_lst = []

for i in range(len(lst[0])-1, -1, -1):
	new_lst = []
	for el in lst:
		new_lst.append(el[i])
	big_lst.append(new_lst)


print(big_lst)
