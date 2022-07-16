import auxiliar_functions
import time

def exercise41():

	n = 0

	def checkPandigital(number):
		digits = list(str(number))
		
		for i in range(1, n+1):
			if str(i) not in digits:
				return False
		return True

	def main_iteration(initial, last):
		print(f"Starting iteration from {initial} to {last}.")
		
		start_time = time.time()

		for i in range(last, initial, -2):
			if checkPandigital(i):
				if auxiliar_functions.is_prime(i):
					print("Pandigital and prime: " + str(i))
		
		print(f"Finished iteration in {(time.time() - start_time)} seconds")
			
	for i in range(9, 4, -1):
		n = i
		initial = ""
		last = ""
		for j in range(1, i+1):
			initial += str(j)
			last += str(i + 1 - j)
		main_iteration(int(initial), int(last))

if __name__ == '__main__':
	print("takes too long but its right")
	exercise41()