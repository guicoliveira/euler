def exercise4():
	biggest_palindrome = 0
	for i in range(1000, 100, -1):
		for j in range(1000, 100, -1):
			value = str(i * j)
			if value[0] == value[len(value) - 1] and value[1] == value[len(value) - 2] and value[2] == value[len(value) - 3]:
				print(f"{i} * {j} = {value}")
				if int(value) > biggest_palindrome:
					biggest_palindrome = int(value)
				break

	print(f"Result: {biggest_palindrome}")


if __name__ == '__main__':
	exercise4()


# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.
