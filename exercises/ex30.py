def exercise30():
	power = 5
	finalSum = 0


	for i in range(2, 10000000):
		sum = 0
		for d in str(i):
			sum += int(d) ** power
		if sum == i: 
			finalSum += i


	print(f"Result: {finalSum}")

if __name__ == '__main__':
	exercise30()