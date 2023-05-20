def exercise52():
	'''
	Can only go from x to x + (x * 1.666(6))
	Where x is the first number of a new n digits value
	E.g.: 100 - 166, 1000 - 1666, 10000 - 16666
	'''
	initial_digit_value = 10

	result = 0
	while result == 0:
		initial_digit_value = initial_digit_value * 10
		final_digit_value = initial_digit_value * (5/3)
		for i in range(initial_digit_value, int(final_digit_value)):
			if compare_multiples_digits(i):
				result = i
				print(f"Result: {i}")
				break


def compare_multiples_digits(val) -> bool:
	digits = sorted(list(str(val)))
	aux = val
	for i in range(1, 6):
		aux = aux + val
		if sorted(list(str(aux))) != digits:
			return False
	return True

'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''