def exercise13():
	f = open("aux_files\\100_50digit.txt", "r")
	total_sum = 0
	for i in range(100):
		number = f.readline()
		total_sum += int(number)
	print(f"Result: {total_sum}")


if __name__ == '__main__':
	exercise13()