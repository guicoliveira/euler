
def sortAndCheckNumber(string):
	sortedStr = sorted(string)
	for k in range(9):
		if sortedStr[k] != str(k+1):
			return False
	return True


def exercise38():



	bestMatch = 0
	bestPandigital = 0

	for n in range(2, 10):
		for i in range(1, 800000):
			auxStr = ""
			for j in range(1, n+1):
				auxStr += str(i * j)
			if len(auxStr) > 9:
				break
			elif len(auxStr) < 9:
				continue
			else:
				if sortAndCheckNumber(auxStr) and int(auxStr) > bestPandigital:
					bestPandigital = int(auxStr)
					bestMatch = i

	print(f"Result: {bestPandigital}.")


if __name__ == '__main__':
	exercise38()