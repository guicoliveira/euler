from auxiliar_functions import get_next_prime_number, is_prime

def exercise50():
	prime_numbers = [2]
	limit = 1000000

	while prime_numbers[len(prime_numbers) - 1] < limit:
		prime_numbers.append(get_next_prime_number(prime_numbers[len(prime_numbers) - 1]))

	longest_streak = 0
	result = 0

	for i in range(len(prime_numbers) - 1):
		initial_number = prime_numbers[i]
		calc = prime_numbers[i]
		for j in range(i+1, len(prime_numbers) - 1):
			calc = calc + prime_numbers[j]
			if calc > limit:
				break
			if is_prime(calc):
				if longest_streak <= j - i + 1:
					#print(f"New entry: started: {initial_number}, total: {calc}, n primes: {j - i+ 1}")
					result = calc
					longest_streak = j - i + 1

	print(f"Result: {result}")

if __name__ == '__main__':
	exercise50()