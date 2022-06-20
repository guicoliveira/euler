def exercise16():
	num = 2
	for i in range(999):
		num = num * 2

	num_str = str(num)
	print(len(num_str))

	result = int(num_str[0])
	for j in range(1, len(num_str)):
		#print('result is:', result, '; adding:', num_str[j])
		result = result + int(num_str[j])

	print(f"Result: {result}")


if __name__ == '__main__':
	exercise16()