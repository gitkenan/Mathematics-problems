# How many prime numbers are there between 1 and 999?

primes = []

for possibility in range(2, 3000000):
	isPrime = True
	for num in range(2, possibility):
		if possibility % num == 0:
			isPrime = False
		else:
			pass
	if isPrime:
		primes.append(possibility)
	else:
		pass

print primes
print len(primes)
