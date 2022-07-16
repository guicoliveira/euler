import time
import auxiliar_functions


def exercise12():
	triangle_number = 0
	aux = 1
	max_divisors = 0
	while 1:
		while 1:
			triangle_number += aux
			aux += 1
			if (triangle_number % 2) == 0:
				break
		divisors = auxiliar_functions.get_divisors(triangle_number)
		if divisors > max_divisors:
			max_divisors = divisors
			print(triangle_number, ': ', max_divisors)

		if divisors > 500:
			print(f"Result: {triangle_number} - divisors: {divisors}")
			break


if __name__ == '__main__':
	exercise12()