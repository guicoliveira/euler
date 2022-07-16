import auxiliar_functions

def removeRightDigit(digits):
	for i in range(len(digits)-1):
		digits = digits[:-1]
		if not auxiliar_functions.is_prime(int(digits)):
			return False

	return True

def removeLeftDigit(digits):
	for i in range(len(digits)-1):
		digits = digits[1:]
		if int(digits) == 1:
			return False
		if auxiliar_functions.is_prime(int(digits)) == False:
			return False

	return True

def has_even_digit(digits):
	if int(digits[0]) % 2 == 0 and int(digits[0]) != 2:
		return True

	if len(digits) < 3:
		return False

	for i in range(1, len(digits)-1):
		if int(digits[i]) % 2 == 0:
			return True

	return False

def exercise37():
	sum = 0
	count = 0
	i = 10
	while count < 11:
		i = auxiliar_functions.get_next_prime_number(i)
		#print(f"Number {i} =======================")
			
		digits = str(i)

		if digits[0] == '1' or digits[len(digits)-1] == '1':
			continue
		
		if has_even_digit(digits):
			continue

		if removeRightDigit(str(i)) and removeLeftDigit(str(i)):
			sum += i
			count += 1        
			print("Adding " + str(i) + " to the sum ("+str(sum)+") and count("+str(count)+")")

		i += 1

	print(f"Result: {sum}")

if __name__ == '__main__':
	exercise37()