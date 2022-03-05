import fractions
import string
from tokenize import Double


class Fraction:
	numerator:int
	denominator:int
	result:float


def get_possible_results():
	possible_results = []
	for numerator in range(1, 10):
		for denominator in range(numerator+1, 10):
			res = numerator /denominator
			fraction = Fraction()
			fraction.numerator = numerator
			fraction.denominator = denominator
			fraction.result = res
			possible_results.append(fraction)
	return possible_results


def exercise33():
	possible_results = get_possible_results()

	numerators = []
	denominators = []

	for numerator in range(10, 100):
		for denominator in range(numerator+1, 100):
			result = numerator /denominator
			for fraction in possible_results:
				if fraction.result == result:
					#if the number exists 
					numerator_str = str(numerator)
					denominator_str = str(denominator)
					if str(fraction.numerator) in numerator_str and str(fraction.denominator) in denominator_str:
						if numerator / 10 == fraction.numerator:
							continue
						
						removed_numerator_digit = ""
						if numerator_str[0] == str(fraction.numerator):
							removed_numerator_digit = numerator_str[1]
						else:
							removed_numerator_digit = numerator_str[0]
							
						removed_denominator_digit = ""
						if denominator_str[0] == str(fraction.denominator):
							removed_denominator_digit = denominator_str[1]
						else:
							removed_denominator_digit = denominator_str[0]

						if removed_denominator_digit == removed_numerator_digit:
							numerators.append(numerator)
							denominators.append(denominator)
							print(f"{numerator}/{denominator} = {fraction.numerator}/{fraction.denominator} = {result}")

	final_numerator = 0
	for n in numerators:
		if final_numerator == 0:
			final_numerator = n
		else:
			final_numerator = final_numerator * n


	final_denominator = 0
	for d in denominators:
		if final_denominator == 0:
			final_denominator = d
		else:
			final_denominator = final_denominator * d

	final_result = final_numerator / final_denominator
	print(f"{final_numerator} / {final_denominator} = {final_result} ")

	i = 1
	aux = final_result
	while aux <= 1:
		aux += final_result
		i += 1

	print(f"Result: {i}")


if __name__ == '__main__':
	exercise33()