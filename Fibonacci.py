def fibonacci(n):
	if n<=0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

n = int(input('Enter a positive number: '))
print('The', n, 'th fibonacci number is', fibonacci(n))
