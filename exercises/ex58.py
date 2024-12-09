from auxiliar_functions import is_prime
def exercise58():
	position = 1
	line = 0
	total_corners = 0
	total_primes = 0
	prime_percentage = 100
	layers = 0

	while prime_percentage > 10:
		line += 2
		position += 1
		position = position + line - 1
		total_corners += 4
		if is_prime(position):
			total_primes += 1
		for _ in range(3):
			position += line
			if is_prime(position):
				total_primes += 1
		prime_percentage = (total_primes / total_corners) * 100
		layers += 1
		# print(f"Layer #{layers}:\t{prime_percentage}")
		result = (layers * 2) + 1

	print(f"Result: {result}")


if __name__ == '__main__':
	exercise58()
