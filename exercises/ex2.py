def exercise2():
	fibonacci_aux = 1
	fibonacci = 2
	sum = 2
	while fibonacci < 4000000:
		aux = fibonacci
		fibonacci = fibonacci + fibonacci_aux
		fibonacci_aux = aux	
		if fibonacci % 2 == 0:
			sum += fibonacci

	print(f"Result {sum}")
	
if __name__ == '__main__':
	exercise2()