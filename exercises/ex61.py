from dataclasses import dataclass


@dataclass
class Polygonal:
	polygonal_type: int
	n: int
	result: int


def triangle(n: int) -> int:
	return int((n * (n + 1)) / 2)


def square(n: int) -> int:
	return int(n * n)


def pentagonal(n: int) -> int:
	return int((((3 * n) - 1) * n) / 2)


def hexagonal(n: int) -> int:
	return int(((2 * n) - 1) * n)


def heptagonal(n: int) -> int:
	return int((((5 * n) - 3) * n) / 2)


def octagonal(n: int) -> int:
	return int(((3 * n) - 2) * n)
	
	
def get_polygonals(pol_type: int) -> list[Polygonal]:
	result = []
	if pol_type == 3:
		method = triangle
	elif pol_type == 4:
		method = square
	elif pol_type == 5:
		method = pentagonal
	elif pol_type == 6:
		method = hexagonal
	elif pol_type == 7:
		method = heptagonal
	elif pol_type == 8:
		method = octagonal
	else:
		raise Exception("Wrong polygonal type")
	
	for i in range(1, 10):
		pol = method(i)
		if pol > 10000:
			return result
		result.append(Polygonal(polygonal_type=pol_type, n=i, result=pol))
	return result


def exercise61():
	p3 = get_polygonals(3)
	p4 = get_polygonals(4)
	p5 = get_polygonals(5)
	p6 = get_polygonals(6)
	p7 = get_polygonals(7)
	p8 = get_polygonals(8)

	print([p.result for p in p3])
	print([p.result for p in p4])
	print([p.result for p in p5])
	print([p.result for p in p6])
	print([p.result for p in p7])
	print([p.result for p in p8])

	print("Result:")

	test = ["rege", "geve", "dmweio"]
	result = ", ".join(test)
	print(result)

if __name__ == '__main__':
	exercise61()
