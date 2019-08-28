# Sum all numbers in the Fibbonacci sequence under 4,000,000

total = 0
a, b = 1, 0
while b <= 4000000:
	if b % 2 == 0:
		total += b
	a, b = b, a + b		# to continually assign a to b and b to a + b
print total


