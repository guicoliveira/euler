from math import factorial

def exercise53():
	result = 0
	for number in range(23, 101):
		for i in range(1, number):
			if calculate_total_combinations(number, i) > 1000000:
				result += 1
	print(f"Result {result}")


def calculate_total_combinations(n_digits, combination_size):
	return factorial(n_digits) / (factorial(combination_size) * factorial(n_digits - combination_size))
