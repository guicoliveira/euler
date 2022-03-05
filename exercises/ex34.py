def calc_factorial(number):
    total = number
    for i in range(number-1, 0, -1):
        total = total * i
    return total

def exercise34():
	for i in range(10, 1499999):
		sumTotal = 0
		for digit in str(i):
			digit_factorial = calc_factorial(int(digit))
			sumTotal += digit_factorial
		if sumTotal == i:
			print(str(i) + ": " + str(sumTotal))

if __name__ == '__main__':
	exercise34()