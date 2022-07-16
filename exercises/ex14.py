from typing import Dict, List


def exercise14():
	"""
	To every number n between 0 and 1 million
	If n is even divide it by 2
	If n is off multiply it by 3 and add 1
	End iterations when n == 1
	Finds the biggest train (number of iterations) and corresponding number
	"""
	number_results = {}
	train = 0
	number = 0

	for i in range(2, 1000001):
		n = i
		n_iterations = 0
		while 1:
			if (n % 2) == 0:
				n = n / 2
			else:
				n = (n * 3) + 1
			n_iterations += 1

			if n < i and n != 1:
				n_iterations += number_results[int(n)]
				n = 1

			if n == 1:
				number_results[int(i)] = int(n_iterations)
				#print(f"{i} - {n_iterations} iterations")
				if train < n_iterations:
					train = n_iterations
					number = i

				break

	print(number, ' - ', train)


if __name__ == '__main__':
	exercise14()