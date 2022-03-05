def exercise40():
	strAux = ""
	for i in range(190000):
		strAux += str(i)


	result = int(strAux[1]) * int(strAux[10]) * int(strAux[100]) * int(strAux[1000]) * int(strAux[10000]) * int(strAux[100000]) * int(strAux[1000000])
	print(result)

if __name__ == '__main__':
	exercise40()