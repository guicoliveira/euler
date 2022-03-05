import auxiliarFunctions

def rotate_digits(digits, length):
    aux = ""

    for i in range(1, length):
        aux += digits[i]
    aux += digits[0]

    return aux

def digits_array_to_int(digits, length):
    strTest = ""
    for i in range(length):
        strTest += digits[i]
    
    return int(strTest)

def check_rotations(number):
    digits = str(number)

    length = len(digits)
    if length == 1:
        return True

    for i in range(length-1):
        digits = rotate_digits(digits, length)
        if not auxiliarFunctions.is_prime(int(digits)):
            return False

    return True

def exercise35():
	count = 0

	for i in range(2, 1000000):		
		if not auxiliarFunctions.is_prime(i):
			continue

		if not check_rotations(i):
			continue
		count += 1

	print(f"Result: {count}.")

if __name__ == '__main__':
	exercise35()