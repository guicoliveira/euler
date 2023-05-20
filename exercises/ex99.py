def exercise99():
	test = []
	test1 = []
	for i in range(99999):
		test.append(i)
		test1.append(99998 - i)

	print(test == test1)
	test1.sort()
	print(test == test1)


	# for n in test:
	# 	if n not in test1:
	# 		print(f"{n} is not in test1")
	# 		break



if __name__ == '__main__':
	exercise99()