# What is the sum of all palindrome numbers under 100000?

palindromes = []

for n in range(1, 100000):

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

# factors = []
# to make a set of factors which make up palindromes
# for p in palindromes:
# 	for n in range(100, 1000):
# 		if p % n == 0:
# 			factors.append(n)
# 		else:
# 			pass


print palindromes
print "The sum of all the palindromes between 1 and 100,000 is", sum(palindromes)

