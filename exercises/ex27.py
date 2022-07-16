import auxiliar_functions

def exercise27():

	best_a = 0
	best_b = 0
	number_of_primes = 0

	for a in range(-999, 1000):
		for b in range(-1000, 1001):
			n = 0
			while True:
				result = (n ** 2) + (n * a) + b
				if not auxiliar_functions.is_prime(result):
					if n > number_of_primes:
						number_of_primes = n
						best_a = a
						best_b = b				
					break	
				n += 1
	
	print(f"Result: {best_a} * {best_b} = {best_a * best_b}")

if __name__ == '__main__':
	exercise27()