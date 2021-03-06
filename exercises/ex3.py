import auxiliar_functions

def exercise3():
	value = 600851475143
	i = 2
	primes_used = []
	while not auxiliar_functions.is_prime(value):
		print(i)		
		if value % i == 0:
			primes_used.append(i)
			value = value / i
			i = 2

		i = auxiliar_functions.get_next_prime_number(i)

	print(f"Result {value}")
	print(f"Primes used: {primes_used}")

if __name__ == '__main__':
	exercise3()




# The prime factors of 13195 are 5, 7, 13 and 29.
# 13195 /  5
# 13195 / 5
# 2639 /  7

# What is the largest prime factor of the number 600851475143 ?
