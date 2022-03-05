class CoinCollection:
    def __init__(self, one, two, five, ten, twenty, fifty, hundred, twohundred):
        self.one = one
        self.two = two
        self.five = five
        self.ten = ten
        self.twenty = twenty
        self.fifty = fifty
        self.hundred = hundred
        self.twohundred = twohundred

    def calculateDepth(self):
        depth = self.one + self.two  + self.five + self.ten + self.twenty + self.fifty + self.hundred + self.twohundred 
        return depth
    
    def calculateSum(self):
        sum = (self.one) + (self.two * 2) + (self.five * 5) + (self.ten * 10) + (self.twenty * 20) + (self.fifty * 50) + (self.hundred * 100) + (self.twohundred * 200)
        return sum

    def __str__(self):
        return "1p: " + str(self.one) + "; 2p: " + str(self.two) + "; 5p: " + str(self.five) + "; 10p: " + str(self.ten) + "; 20p: " + str(self.twenty) + "; 50p: " + str(self.fifty) + "; 100p: " + str(self.hundred) + "; 200p: " + str(self.twohundred)

class Node:
    def __init__(self, one, two, five, ten, twenty, fifty, hundred, twohundred):
        self.collection = CoinCollection(one, two, five, ten, twenty, fifty, hundred, twohundred)
        self.depth = self.collection.calculateDepth()
        if(self.collection.calculateSum() == 200):
            global totalWays
            totalWays += 1
            ##print(self)
        else:
            self.addChildren()
        
    def addChildren(self):
        if self.collection.calculateSum() + 200 <= 200 and self.collection.one == 0 and self.collection.two == 0 and self.collection.five == 0 and self.collection.ten == 0 and self.collection.twenty == 0 and self.collection.fifty == 0 and self.collection.hundred == 0:
            Node(self.collection.one, self.collection.two, self.collection.five, self.collection.ten, self.collection.twenty, self.collection.fifty, self.collection.hundred, self.collection.twohundred + 1) 
        if self.collection.calculateSum() + 100 <= 200 and self.collection.one == 0 and self.collection.two == 0 and self.collection.five == 0 and self.collection.ten == 0 and self.collection.twenty == 0 and self.collection.fifty == 0:
            Node(self.collection.one, self.collection.two, self.collection.five, self.collection.ten, self.collection.twenty, self.collection.fifty, self.collection.hundred + 1, self.collection.twohundred) 
        if self.collection.calculateSum() + 50 <= 200 and self.collection.one == 0 and self.collection.two == 0 and self.collection.five == 0 and self.collection.ten == 0 and self.collection.twenty == 0:
            Node(self.collection.one, self.collection.two, self.collection.five, self.collection.ten, self.collection.twenty, self.collection.fifty + 1, self.collection.hundred, self.collection.twohundred) 
        if self.collection.calculateSum() + 20 <= 200 and self.collection.one == 0 and self.collection.two == 0 and self.collection.five == 0 and self.collection.ten == 0:
            Node(self.collection.one, self.collection.two, self.collection.five, self.collection.ten, self.collection.twenty + 1, self.collection.fifty, self.collection.hundred, self.collection.twohundred) 
        if self.collection.calculateSum() + 10 <= 200 and self.collection.one == 0 and self.collection.two == 0 and self.collection.five == 0:
            Node(self.collection.one, self.collection.two, self.collection.five, self.collection.ten + 1, self.collection.twenty, self.collection.fifty, self.collection.hundred, self.collection.twohundred) 
        if self.collection.calculateSum() + 5 <= 200 and self.collection.one == 0 and self.collection.two == 0:
            Node(self.collection.one, self.collection.two, self.collection.five + 1, self.collection.ten, self.collection.twenty, self.collection.fifty, self.collection.hundred, self.collection.twohundred) 
        if self.collection.calculateSum() + 2 <= 200 and self.collection.one == 0:
            Node(self.collection.one, self.collection.two + 1, self.collection.five, self.collection.ten, self.collection.twenty, self.collection.fifty, self.collection.hundred, self.collection.twohundred) 
        if self.collection.calculateSum() + 1 <= 200:
            Node(self.collection.one + 1, self.collection.two, self.collection.five, self.collection.ten, self.collection.twenty, self.collection.fifty, self.collection.hundred, self.collection.twohundred) 

    def __str__(self):
        return "Depth: " + str(self.depth) + ";\t" + str(self.collection) + "; - Sum: " + str(self.collection.calculateSum())

def exercise31():
	totalWays = 0
	collection = CoinCollection(0, 0, 0, 0, 0, 0, 0, 0)
	node = Node(0, 0, 0, 0, 0, 0, 0, 0)

	print(f"Result: {totalWays}")



if __name__ == '__main__':
	exercise31()