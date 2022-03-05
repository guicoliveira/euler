
def decimal_to_binary(num):
    aux = list(bin(num))
    aux = aux[2:len(aux)]
    return aux


def is_palindromic(digits):    
    length = len(digits)
    for i in range(length // 2):
        if not digits[i] == digits[length - i - 1]:
            return False

    return True

def exercise36():
	sum = 0

	for i in range(1000000):
		array = []
		digits = list(str(i))
		digitsBin = decimal_to_binary(i)

		if is_palindromic(digits) and is_palindromic(digitsBin):
			sum += i

	print(f"Result: {sum}.")

if __name__ == '__main__':
	exercise36()