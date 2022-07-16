def exercise9():
	found = False

	for c in range(999):
		if found:
			break
		for b in range(999):
			if (b >= c) or found:
				break
			for a in range(999):
				if (a >= b) or found:
					break
				if ((a * a) + (b * b) == (c * c)) and a + b + c == 1000:
					print(a, ' - ', b, ' - ', c)
					product = a * b * c
					print(f"Result: {product}")
					found = True


if __name__ == '__main__':
	exercise9()