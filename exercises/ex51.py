from auxiliar_functions import is_prime

def exercise51():
	print("it's not working")
	return
	values = replace_digits(12345, len(str(12345)))
	for val in values:
		print(val)
	# highest_prime_value = 0
	# i = 100
	#
	# while highest_prime_value < 8 or i < 110:
	# 	i += 1
	# 	digits_length = len(str(i))
	# 	if not is_prime(i):
	# 		continue
	#
	# 	# generate_values_from_n_digits(n_digits)
	# 	replace_digits(i, digits_length)




def replace_digits(value, n_digits):
	all_wildcards_possibilites = []
	for digits_to_replace in range(1, n_digits): # will run a ccicle for each number until n digits
		# print(f"Changing {digits_to_replace} digits")
		all_wildcards_possibilites = all_wildcards_possibilites + generate_values_wildcards(value, digits_to_replace, n_digits)

	best_family_owner = 0
	best_prime_count = 0

	for val in all_wildcards_possibilites:
		best_family_owner = 0
		best_prime_count = 0
		for i in range(10):
			for element in val:
				if element == "*":
					element = i
			if is_prime(int("".join(val))):
				print("I GIve up")


	return all_wildcards_possibilites

def generate_values_wildcards(value, digits_to_replace, n_digits):
	# generate_possible_values(value_list, new_digit, level-1, n_digits,all_possible_values)
	values_wildcards = []
	if digits_to_replace == 1:
		for i in range(n_digits):
			aux_value = list(str(value))
			aux_value[i] = "*"
			# print(f"Appending {aux_value}")
			values_wildcards.append(aux_value)

	elif digits_to_replace == (n_digits - 1):
		for i in range(n_digits):
			aux_value = list(str(value))
			for j in range(n_digits):
				if i == j:
					continue
				aux_value[j] = "*"
			values_wildcards.append(aux_value)

	else:
		return generate_intermediate_values(value, n_digits, digits_to_replace, 0, 0)

	return values_wildcards

def generate_intermediate_values(value, n_digits, digits_to_replace, starting_point, level):
	if level == digits_to_replace:
		return [list(str(value))]
	possibilities = []
	for i in range(starting_point, (n_digits - digits_to_replace + level + 1)):
		aux_possibilities = generate_intermediate_values(value, n_digits, digits_to_replace, i + 1, level + 1)
		for poss in aux_possibilities:
			poss[i] = "*"
		possibilities = possibilities + aux_possibilities
	return possibilities



# 	while highest_prime_value < 8 and i < 1000000:
# 		i += 1
#
# 		if i % 10000 == 0:
# 			print(i)
#
# 		if i % 2 == 0:
# 			continue
#
# 		best_family_owner, max_n_primes = selecting_positions(i)
# 		if highest_prime_value < max_n_primes:
# 			highest_prime_value = max_n_primes
# 			print(f"{best_family_owner} has {max_n_primes} primes")
#
# 	print(f"Result: ")
#
#
# def selecting_positions(value):
# 	value_digits = len(str(value))
# 	max_n_primes = 0
# 	best_family_owner = 0
# 	# print(f"{value} -------------- Value: {value}")
# 	for i in range(value_digits):
# 		for j in range(i + 1, value_digits + 1):
# 			n_primes, family_owner = each_iteration(value, value_digits, i, j)
# 			if n_primes > max_n_primes:
# 				max_n_primes = n_primes
# 				best_family_owner = family_owner
#
# 	return best_family_owner, max_n_primes
#
#
# def each_iteration(value, length, pos1, pos2):
# 	total_primes = 0
# 	first_prime = 0
# 	for i in range(10):
# 		initial = ['*' for _ in range(length + 2)]
# 		initial[pos1] = str(i)
# 		initial[pos2] = str(i)
# 		placed_letters = 0
# 		for k in range(len(initial)):
# 			if initial[k] == "*":
# 				initial[k] = str(value)[placed_letters]
# 				placed_letters += 1
# 		if initial[0] == "0":
# 			continue
# 		final_value = int("".join(initial))
# 		if is_prime(final_value):
# 			# print(final_value)
# 			if first_prime == 0:
# 				first_prime = final_value
# 			total_primes += 1
#
#
# 	return total_primes, first_prime

