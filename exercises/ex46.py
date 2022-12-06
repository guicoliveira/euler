from math import sqrt

from auxiliar_functions import get_next_prime_number, is_odd_composite_number

def has_divider(i, primes):
	for prime in primes:
		for j in range(1, i):
			aux = prime + ((j * j) * 2)
			#print(f"{i} == {aux} : {prime} + (({j} * {j}) * 2)")
			if aux > i:
				break
			if aux == i:
				return True
	return False

def exercise46():
	prime_numbers = [2]

	for i in range(9, 50000):
		if not is_odd_composite_number(i):
			continue

		while prime_numbers[len(prime_numbers) - 1] < i:
			prime_numbers.append(get_next_prime_number(prime_numbers[len(prime_numbers) - 1]))

		if not has_divider(i, prime_numbers):
			print(f"Result: {i}")
			break

if __name__ == '__main__':
	exercise46()
