def exercise48():
	result = 0
	for i in range(1, 1000):
		result += i ** i

	print(f"Result: {str(result)[-10:]}")


if __name__ == '__main__':
	exercise48()