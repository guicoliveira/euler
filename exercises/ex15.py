def exercise15():
	n = 20
	aux = n + 1
	bi_array = [[0 for x in range(aux)] for y in range(aux)]

	bi_array[n - 1][n] = 1
	bi_array[n][n - 1] = 1

	for i in range(2, (n * 2) + 1):
		for j in range(i + 1):
			if (n - j) == 20:
				bi_array[n - i + j][n - j] = bi_array[n - i + j + 1][n - j]
			elif (n - i + j) == 20:
				bi_array[n - i + j][n - j] = bi_array[n - i + j][n - j + 1]
			else:
				bi_array[n - i + j][n - j] = bi_array[n - i + j + 1][n - j] + bi_array[n - i + j][n - j + 1]

	# for k in range(n + 1):
		# print(k, '-\t', bi_array[k])

	print(f"Result: {bi_array[0][0]}")


if __name__ == '__main__':
	exercise15()