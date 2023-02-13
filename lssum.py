ls = []
n = int(input('Enter a length: '))
for i in range(n):
	num = int(input('Enter a number: '))
	ls.append(num)

sum = 0
for i in ls:
	sum = sum + int(i)

print('The sum of its elements is ', sum)
