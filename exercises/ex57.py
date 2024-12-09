def execute_iteration(denominator: int, numerator: int):
	new_denominator = (denominator * 2) + numerator
	new_numerator = denominator

	return new_denominator, new_numerator


def exercise57():
	denominator = 2
	numerator = 1
	total = 0
	for i in range(1000):
		real_numerator = numerator + denominator
		# print(f"{i} - {real_numerator} / {denominator}")
		if len(str(real_numerator)) > len(str(denominator)):
			total += 1
		denominator, numerator = execute_iteration(denominator, numerator)

	print(f"Result: {total}")


if __name__ == '__main__':
	exercise57()
