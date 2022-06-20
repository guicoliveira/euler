import auxiliar_functions


def exercise7():
	prime = 0
	for i in range(10000):
		prime = auxiliar_functions.get_next_prime_number(prime)
	print(f"Result: {prime}")


if __name__ == '__main__':
	exercise7()