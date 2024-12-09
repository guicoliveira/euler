def calculate_digital_sum(number: int) -> int:
	total = 0
	for c in str(number):
		total += int(c)
	return total


def exercise56():
	biggest_digital_sum = 0
	best_value = 0
	best_power = 0
	for i in range(1, 100):
		for j in range(1, 100):
			value = i ** j
			digital_sum = calculate_digital_sum(value)
			if biggest_digital_sum < digital_sum:
				biggest_digital_sum = digital_sum
				best_value = i
				best_power = j
	print(f"Result: {biggest_digital_sum} - {best_value}^{best_power} = {best_value ** best_power}")


if __name__ == '__main__':
	exercise56()


'''
A googol (10^100) is a massive number: one followed by one-hundred zeros; 
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
'''