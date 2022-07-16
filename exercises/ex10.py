def exercise10():
	n = 2000000
	total_sum = 0
	array = [True] * n

	for p in range(2, n):
		if array[p]:
			total_sum += p
			for i in range(p * p, n, p):
				array[i] = False
	print(f"Result: {total_sum}")


if __name__ == '__main__':
	exercise10()