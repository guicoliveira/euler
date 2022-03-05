def twoEqualDigitsInArray(array):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return True

def exercise32():
	sum_array = []

	for i in range(2000):
		for j in range(i+1, 100000):
			multiplicand = i
			multiplier = j
			product = i * j

			alldigits = [int(i) for i in str(multiplicand)]
			alldigits += [int(i) for i in str(multiplier)]
			alldigits += [int(i) for i in str(product)]

			if len(alldigits) < 9:
				continue
			elif len(alldigits) > 9:
				break

			if 0 in alldigits:
				continue

			if twoEqualDigitsInArray(alldigits):
				continue
			
			print(f"{multiplicand} * {multiplier} = {product}")
			if product not in sum_array:
				sum_array.append(product)
	sum = 0
	for value in sum_array:
		sum += value
	print(f"Result {sum}")


if __name__ == '__main__':
	exercise32()