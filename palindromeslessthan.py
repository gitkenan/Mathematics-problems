# What is the sum of all palindrome numbers under 100000?

palindromes = []

for n in range(100000, 1000000):

	temp = n
	rev = 0

	while n > 0:
		digit = n % 10
		rev = rev*10 + digit
		n = n / 10

	if temp == rev:
			palindromes.append(temp)
	else:
		pass

factors = []

for p in palindromes:
	for n in range(100, 1000):
		if p % n == 0:
			factors.append(n)
		else:
			pass


print palindromes
print "The sum of all the palindromes between 100,000 and 1,000,000 is", sum(palindromes)


print factors