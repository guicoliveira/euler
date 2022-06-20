def exercise1():
	sum = 0
	for i in range(1000):
		if i % 3 == 0 or i % 5 == 0:
			sum += i
	
	print(f"Result: {sum}")


if __name__ == '__main__':
	exercise1()
