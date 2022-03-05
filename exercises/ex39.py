import math

def checkAngle(A, B, C):
	#print("Sides: A:"+str(A)+"; B:"+str(B)+"; C:"+str(C)+";")
	angle = math.degrees(math.acos((pow(A, 2) + pow(B, 2) - pow(C, 2)) / (2 * A * B)))
	return angle

def exercise39():
	

	bestMatch = 0
	bestCount = 0

	for i in range(800, 850):
		count = 0
		#print("Perimeter: " + str(i))
		for sideB in range(1, int((i/2) + 1)):
			for sideA in range(1, sideB):
				sideC = math.sqrt(pow(sideB, 2) + pow(sideA, 2))
				if sideC + sideA + sideB == i:
					resultAngle = checkAngle(sideA, sideB, sideC)
					if int(resultAngle) == 90:
						count +=1
		if count >= bestCount:
			bestMatch = i
			bestCount = count
			#print(str(bestMatch) + " - counts: " + str(bestCount))

	print(f"Result: {bestMatch}, {bestCount} counts.")


if __name__ == '__main__':
	exercise39()