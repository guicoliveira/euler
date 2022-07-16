def exercise6():
	squareOfSums = 0
	sumSquares = 0
	for i in range(1, 101):
		sumSquares += (i * i)
		squareOfSums += i

	squareOfSums = squareOfSums * squareOfSums

	result = squareOfSums - sumSquares
	print(f"Result: {result}")


if __name__ == '__main__':
	exercise6()