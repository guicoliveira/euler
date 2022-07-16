import auxiliar_functions


def exercise17():
	total_string = ""

	for i in range(1, 1000):
		add = auxiliar_functions.start_writing_number(str(i))
		#print(add)
		total_string += add

	total_string += "onethousand"
	print(f"Result: {len(total_string)}")


if __name__ == '__main__':
	exercise17()