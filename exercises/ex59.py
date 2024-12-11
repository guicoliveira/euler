import os


def find_key(encrypted_values: list[str]) -> list[int]:
	for i in range(97, 123):
		for j in range(97, 123):
			for k in range(97, 123):
				result = ""
				for l in range(0, len(encrypted_values), 3):
					first = chr(int(encrypted_values[l]) ^ i)
					# print(f"{encrypted_values[l]} XOR {i} ({chr(i)}) = {first}")
					second = chr(int(encrypted_values[l + 1]) ^ j)
					# print(f"{encrypted_values[l + 1]} XOR {j} ({chr(j)}) = {second}")
					third = chr(int(encrypted_values[l + 2]) ^ k)
					# print(f"{encrypted_values[l + 2]} XOR {k} ({chr(k)}) = {third}")
					result += first
					result += second
					result += third
				if "the" not in result or "Euler" not in result:
					continue
				print(f"{result} - key: {chr(i)}{chr(j)}{chr(k)}")
				return [i, j, k]


def get_total_ascii_value(values: list[str], key: list[int]) -> int:
	position = 0
	result = 0
	str_result = ""
	for value in values:
		use_value_in_position = position % 3
		aux = int(value) ^ key[use_value_in_position]
		result += aux
		str_result += chr(aux)
		position += 1

	print(f"Final message: {str_result}")
	result = 0
	for letter in str_result:
		result += ord(letter)
	return result


def exercise59():
	file_path = f"{os.getcwd()}\\aux_files\\p059_cipher.txt"
	file = open(file_path, "r")
	encrypted_message = file.readline()
	encrypted_values = encrypted_message.split(",")

	# key is exp
	key_ints = find_key(encrypted_values)
	result = get_total_ascii_value(encrypted_values, key_ints)

	print(f"Result: {result}")


if __name__ == '__main__':
	exercise59()


'''
Each character on a computer is assigned a unique code and the preferred standard is ASCII. 
For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, 
then XOR each byte with a given value, taken from a secret key. 
The advantage with the XOR function is that using the same encryption key on the cipher text, 
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
65 = 0100 0001
42 = 0010 1010
XOR = 0110 1011 = 107

space = 32 = 00100000
		88 = 01011000
		   = 01111000

For unbreakable encryption, the key is the same length as the plain text message, 
and the key is made up of random bytes. 
The user would keep the encrypted message and the encryption key in different locations, 
and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. 
If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. 
The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. 
Using p059_cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, 
and the knowledge that the plain text must contain common English words, 
decrypt the message and find the sum of the ASCII values in the original text.
'''