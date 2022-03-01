def exercise5():

	value = 2
	found = False
	mid_stage = False
	
	while not found:
		# 19, 17, 15, 13, 11
		for i in range(19, 10, -2):
			if value % i != 0:
				value += 2
				break

			if i == 11:
				mid_stage = True
			
		if mid_stage:
			# 20, 18, 16, 14, 12
			for i in range(20, 11, -2):
				if value % i != 0:
					value += 2
					mid_stage = False
					break
			if mid_stage:				
				print(f"Result: {str(value)}")
				found = True
		

if __name__ == '__main__':
	exercise5()


#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?