from decimal import Decimal
import decimal
decimal.setcontext(decimal.Context(prec=10000))


def find_recurring(number: int, digits: str, current_biggest_reccuring: int) -> int:
	if len(digits) < (current_biggest_reccuring * 2):
		return 0
	for offset in range(3):
		for i in range(1, int(len(digits)/3)):
			for j in range(i):
				if digits[offset + i + j] != digits[offset + j]:
					break
				if digits[offset + (i*2) + j] != digits[offset + j]:
					break
			else:
				return i
	return 0


def exercise26():
	biggest_recurring = 0
	biggest_recurring_number = 0
	for i in range(2, 1000):
		value = Decimal(1) / Decimal(i)
		digits = str(value)[2:]
		recurring_value = find_recurring(i, digits, biggest_recurring)

		if recurring_value > biggest_recurring:
			biggest_recurring = recurring_value
			biggest_recurring_number = i

	print(f"Result: {biggest_recurring_number} - recurring value is {biggest_recurring}")


if __name__ == '__main__':
	exercise26()



# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.