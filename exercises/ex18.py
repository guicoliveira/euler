from auxiliarClasses.Tree import *

def exercise18():
	f = open("aux_files\\treeNumbers.txt", "r")
	j = 1
	numbers = []
	for line in f:
		numbers.append(line.split())
		
	arvore = Tree(numbers)
	arvore.getBiggerValue()

if __name__ == '__main__':
	exercise18()