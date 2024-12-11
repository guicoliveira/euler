def exercise63():
	matches = 0
	value = 1
	power = 1
	while True:
		power_result = value ** power
		number_len = len(str(power_result))
		print(f"{value} ** {power} = {power_result}")

		if number_len == power:
			print(f"{power_result} has {power} digits")
			matches += 1
		elif number_len < power:
			pass
		else:
			value = 0
			power += 1
			print(f"\n")
		value += 1

		if power >= 22:
			print(f"Result: {matches}")
			return


if __name__ == '__main__':
	# EXPLANATION: 10 ** N has always N+1 digits, after power 21 there are no matches with value < 10
	exercise63()


'''
The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''