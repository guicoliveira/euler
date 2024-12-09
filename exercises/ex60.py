from typing import Optional

from auxiliar_functions import get_next_prime_number, is_prime


def exercise60():
	new_prime = 11
	primes = [3, 5, 7, 9, 11]
	while True:
		new_prime = get_next_prime_number(new_prime)
		primes.append(new_prime)
		primes_result = find_prime_pair_set(primes)
		if primes_result is not None:
			print(f"Found result with numbers: {primes_result}")
			result = sum(primes_result)
			print(f"Result: {result}")
			return
		print(f"Prime list has {len(primes)} elements")


def find_prime_pair_set(primes: list[int]) -> Optional[list[int]]:
	for i in range(len(primes)):
		for j in range(i+1, len(primes)):
			for k in range(j+1, len(primes)):
				for l in range(k+1, len(primes)):
					for m in range(l+1, len(primes)):
						prime_numbers_to_test = [primes[i], primes[j],  primes[k],  primes[l],  primes[m]]
						if is_prime_pair_set(prime_numbers_to_test):
							return prime_numbers_to_test
	return None


def is_prime_pair_set(primes: list[int]) -> bool:
	for i in range(len(primes)):
		for j in range(i+1, len(primes)):
			if not is_prime_pair(primes[i], primes[j]):
				return False
	return True


def is_prime_pair(first_prime: int, second_prime: int) -> bool:
	first_conc = int(f"{first_prime}{second_prime}")
	if not is_prime(first_conc):
		return False

	second_conc = int(f"{second_prime}{first_prime}")
	if is_prime(second_conc):
		# print(f"Both {first_conc} and {second_conc} are primes")
		return True
	return False


if __name__ == '__main__':
	exercise60()


'''
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''