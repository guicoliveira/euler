from copy import copy

from auxiliar_functions import is_prime, get_next_prime_number


def has_8_family_primes(value: str, pos1: int, pos2: int) -> bool:
	new_value = ""
	for i in range(len(value)):
		if i == pos1 or i == pos2:
			new_value += "0"
		else:
			new_value += value[i]

	possible_prime_count = 10
	new_value = int(new_value)
	pos1_multiplier = pow(10, (len(value) - 1) - pos1)
	pos2_multiplier = pow(10, (len(value) - 1) - pos2)

	if not is_prime(new_value):
		possible_prime_count -= 1

	for j in range(9):
		new_value = new_value + pos1_multiplier
		new_value = new_value + pos2_multiplier
		if not is_prime(new_value):
			possible_prime_count -= 1
			if possible_prime_count < 7:
				return False

	return True


def is_8_family_prime(value: int) -> bool:
	value_str = str(value)
	# number_of_possible_pairs = sum(n for n in range(len(value_str)))
	# print(f"{value} has {number_of_possible_pairs} possible pairs")

	for pos1 in range(2, len(value_str)):  # goes from 1 to (len-1)						pos2,pos1,X
		for pos2 in range(1, pos1):  # goes from 0 to (pos1-1)								pos2,X,pos1
			# here will run all the possible pairs in number[pos1] and number[pos2]		X,pos2,pos1
			if has_8_family_primes(value_str, pos1, pos2):
				print(f"{value} has 8 family primes with positions {pos1} and {pos2}.")
				return True
	return False


def exercise51():
	result = 0
	counter = 0
	while True:
		result = get_next_prime_number(result)
		if is_8_family_prime(result):
			print(f"Result: {result}")
			break
		counter += 1
		if counter % 10000 == 0:
			print(counter)


if __name__ == '__main__':
	exercise51()


# TODO: it's not working, I only did the logic for switching 2 digits in the number and I suppose that I should do it for N-1 digits