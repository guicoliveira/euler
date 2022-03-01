import decimal

decimal.setcontext(decimal.Context(prec=500))

def is_1_digit_recurring(digits):
	if len(digits) > 10:
		aux = digits[len(digits) - 1]
		for i in range(8):
			if digits[len(digits) - 2 - i] != aux:
				return False
	else:
		return False

	return True

def is_2_digit_recurring(digits):
	if len(digits) > 20:
		aux = digits[len(digits) - 1]
		aux2 = digits[len(digits) - 2]
		for i in range(1, 16, 2):
			if digits[len(digits) - 2 - i] != aux or digits[len(digits) - 3 - i] != aux2:
				return False
	else:
		return False

	return True

def is_3_digit_recurring(digits):
	if len(digits) > 30:
		aux = digits[len(digits) - 1]
		aux2 = digits[len(digits) - 2]
		aux3 = digits[len(digits) - 3]
		for i in range(1, 24, 3):
			if digits[len(digits) - 3 - i] != aux or digits[len(digits) - 4 - i] != aux2 or digits[len(digits) - 5 - i] != aux3:
				return False
	else:
		return False

	return True

def is_4_digit_recurring(digits):
	if len(digits) > 40:
		aux = digits[len(digits) - 1]
		aux2 = digits[len(digits) - 2]
		aux3 = digits[len(digits) - 3]
		aux4 = digits[len(digits) - 4]
		for i in range(1, 32, 4):
			if digits[len(digits) - 4 - i] != aux or digits[len(digits) - 5 - i] != aux2 or digits[len(digits) - 6 - i] != aux3 or digits[len(digits) - 7 - i] != aux4:
				return False
	else:
		return False

	return True


def exercise26():

	biggest_value = [0, 0, ""]
	
	for k in range(2, 1000):
		if k != 168:
			continue
		ini = decimal.Decimal(1.0) / decimal.Decimal(k)
		aux = str(ini)
		aux = aux[2:]
		#print(f"Number {k} - {aux}")

		if is_1_digit_recurring(aux) or is_2_digit_recurring(aux) or is_3_digit_recurring(aux) or is_4_digit_recurring(aux):
			#print(f"Number {k} - - {aux}")
			continue
		
		for i in range(int(len(aux) / 2) + 1):
			for j in range(i + 1, len(aux)):
				if aux[i] == aux[j]:
					distance = j - i 
					value1 = aux[i+1:distance]
					value2 = aux[j:j + distance]
					value3 = aux[j + distance:j + distance + distance]
					print(f"1: {value1}; 2: {value2}; 3: {value3}")
					if value1 == value2 and value1 == value3 and len(value1) > 5:
						print(f"found smallest cicle - {k} - {len(value1)} - {value1}")
						break
					if biggest_value[0] < len(value1):
						biggest_value[0] = len(value1)
						biggest_value[1] = k
						biggest_value[2] = value1


	print(f"Result: {biggest_value}")

#005952380952380952380952380952380952380952380952380952380

if __name__ == '__main__':
	exercise26()



# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.