def exercise20():
	total = 1
	for i in range(100):
		total = total * (i + 1)

	total_sum = 0
	for s in str(total):
		total_sum += int(s)

	print(f"Result: {total_sum}")

if __name__ == '__main__':
	exercise20()