# Sieve of Eratosthenes
def SOE(n):
	primes = [True for i in range(n+1)]
	# print(primes)
	primes[0]=primes[1]=False
	i = 2
	while i <= n//2:
		if(primes[i] == True):
			for j in range(i*2, n+1, i):
				primes[j] = False
		i += 1
	print("All prime Numbers 2 to {} are :: ".format(n))
	for i in range(n+1):
		if primes[i] == True:
			print(i, end="\t")

n = int(input("Enter a Number --> "))
SOE(n)

