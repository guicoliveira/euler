from auxiliar_functions import get_next_prime_number


def has_two_distinct_prime_factors(number, primes):
	for prime in primes:
		for prime_aux in primes:
			if prime == prime_aux:
				continue

			calc = prime * prime_aux

			if calc > number:
				break

			if calc == number:
				return True
	return False


def has_two_distinct_prime_factors_v2(number, primes, used_primes: [], total_consecutives):

	for prime in primes:
		if number % prime != 0:
			continue

		if prime > number:
			return False

		calc = int(number / prime)
		used_primes.append(prime)

		if calc == 1:
			if len(set(used_primes)) >= total_consecutives:
				return True
			#print(used_primes)
			return False

		return has_two_distinct_prime_factors_v2(calc, primes, used_primes, total_consecutives)


def reset_results(results, n_consecutives):
	for i in range(n_consecutives):
		results[i] = 0

def exercise47():
	prime_numbers = [2, 3, 5, 7]
	results = []
	n_consecutives = 4
	consecutives = 0

	for i in range(1, 10000000):
		while prime_numbers[len(prime_numbers) - 1] < i:
			prime_numbers.append(get_next_prime_number(prime_numbers[len(prime_numbers) - 1]))

		if has_two_distinct_prime_factors_v2(i, prime_numbers, [], n_consecutives):
			consecutives += 1
			results.append(i)
		else:
			consecutives = 0
			results.clear()

		if consecutives == n_consecutives:
			print(results)
			return


if __name__ == '__main__':
	exercise47()
