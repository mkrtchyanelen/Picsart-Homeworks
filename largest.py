ls = []
n = int(input('Enter a length: '))
for i in range(n):
	num = int(input('Enter a number: '))
	ls.append(num)

largest_num = ls[0]
for i in ls:
	if largest_num < i:
		largest_num = i

print('The largest number of the list is: ', largest_num)
