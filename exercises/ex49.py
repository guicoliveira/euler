from auxiliar_functions import is_prime, is_list_similar


def exercise49():
	for i in range(1000, 9999):
		if not is_prime(i):
			continue
		for j in range(1, 4500):
			first_sum = i + j
			second_sum = first_sum + j
			if not is_list_similar(list(str(i)), list(str(first_sum))) \
				or not is_list_similar(list(str(i)), list(str(second_sum))):
				continue

			if is_prime(first_sum) and is_prime(second_sum):
				print(f"{i}, {first_sum}, {second_sum}")

if __name__ == '__main__':
	exercise49()