import time
from dataclasses import dataclass
from typing import Optional

N_PERMUTATIONS = 5


@dataclass
class Cube:
	value: int
	initial_value: int
	permutations: list[int]


def is_permutation(value1: int, value2: int) -> bool:
	vl1str = str(value1)
	vl2str = str(value2)
	if len(vl1str) != len(vl2str):
		return False
	value1_str = [letter for letter in vl1str]
	value2_str = [letter for letter in vl2str]
	for letter in value1_str:
		try:
			value2_str.pop(value2_str.index(letter))
		except ValueError:
			return False

	if len(value2_str) == 0:
		return True
	return False


def find_permutations(cubes: list[Cube], new_cube: Cube) -> Optional[int]:
	for c in cubes:
		if is_permutation(c.value, new_cube.value):
			c.permutations.append(new_cube.value)
			new_cube.permutations.append(new_cube.value)
			#print(f"{new_cube.initial_value}[{new_cube.value}] is a permutation of {c.initial_value}[{c.value}]")
			if len(c.permutations) == (N_PERMUTATIONS - 1):
				print(f"{c.initial_value}[{c.value}] has reached {N_PERMUTATIONS} permutations")
				print(c)
				return c.value
	return 0


def exercise62():
	value = 1
	cubes = []
	while True:
		cube_value = value ** 3
		new_cube = Cube(value=cube_value, permutations=[], initial_value=value)
		result = find_permutations(cubes, new_cube)
		if result != 0:
			print(f"Result: {result}")
			break
		cubes.append(new_cube)

		value += 1


if __name__ == '__main__':
	start_time = time.time()
	exercise62()
	print("--- Took %s seconds ---" % (time.time() - start_time))

'''
The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''