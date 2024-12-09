def exercise6():
	square_of_sums = 0
	sum_squares = 0
	for i in range(1, 101):
		sum_squares += (i * i)
		square_of_sums += i

	square_of_sums = square_of_sums * square_of_sums

	result = square_of_sums - sum_squares
	print(f"Result: {result}")


if __name__ == '__main__':
	exercise6()