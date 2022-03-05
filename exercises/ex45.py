def exercise45():
	def get_triangle_result(number):
		return int((number * (number + 1)) / 2)
		
	def get_pentagonal_result(number):
		return int((number * ((3 * number) - 1)) / 2)
		
	def get_hexagonal_result(number):
		return int(number * ((2 * number) - 1))

	triangle_index = pentagonal_index = hexagonal_index = 1
	matches = 0
	iterations = 0

	while True:
		iterations += 1

		triangle_result = get_triangle_result(triangle_index) 
		pentagonal_result = get_pentagonal_result(pentagonal_index) 
		hexagonal_result = get_hexagonal_result(hexagonal_index)

		if triangle_result == pentagonal_result == hexagonal_result:
			#print(f'Number: {triangle_result}; Indexes: {triangle_index} - {pentagonal_index} - {hexagonal_index}')
			matches += 1
			if matches == 3:
				print(f"Result: {triangle_result}")
				break

		if triangle_result <= pentagonal_result and triangle_result <= hexagonal_result:
			triangle_index += 1
		elif pentagonal_result <= triangle_result and pentagonal_result <= hexagonal_result:
			pentagonal_index += 1
		elif hexagonal_result <= triangle_result and hexagonal_result <= pentagonal_result:
			hexagonal_index += 1


if __name__ == '__main__':
	exercise45()