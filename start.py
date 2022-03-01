import time
from auxiliarClasses.Tree import *
import sys
import glob
from exercises import *
import exercises



try:
    exercise_number = int(sys.argv[1])
except ValueError:
    print("First argument must be the number of the exercise.")
    exit()
except IndexError:
    print("Need to choose the exercise number as the first argument. Ex: py start.py 22")
    exit()

try:
    file_to_call = getattr(exercises, f"ex{exercise_number}")
    method_to_call = getattr(file_to_call, f"exercise{exercise_number}")
except AttributeError:
    print(f"No file for exercise {exercise_number}")
    exit()


start_time = time.time()
method_to_call()
print("--- Took %s seconds ---" % (time.time() - start_time))





##46

##45
'''
def get_triangle_result(number):
    return (number * (number + 1)) / 2
    
def get_pentagonal_result(number):
    return (number * ((3 * number) - 1)) / 2
    
def get_hexagonal_result(number):
    return number * ((2 * number) - 1)

triangle_index = pentagonal_index = hexagonal_index = 1
matches = 0
iterations = 0
while True:
    iterations += 1

    triangle_result = get_triangle_result(triangle_index) 
    pentagonal_result = get_pentagonal_result(pentagonal_index) 
    hexagonal_result = get_hexagonal_result(hexagonal_index)

    if triangle_result == pentagonal_result == hexagonal_result:
        print(f'Number: {triangle_result}; Indexes: {triangle_index} - {pentagonal_index} - {hexagonal_index}')
        matches += 1
        if matches == 3:
            break

    if triangle_result <= pentagonal_result and triangle_result <= hexagonal_result:
        triangle_index += 1
    elif pentagonal_result <= triangle_result and pentagonal_result <= hexagonal_result:
        pentagonal_index += 1
    elif hexagonal_result <= triangle_result and hexagonal_result <= pentagonal_result:
        hexagonal_index += 1
'''

#41

'''
def secondStep(digits, i):
    for i in range(9):
        if int(digits[i]) == i:
            return True
    return False
        
def checkPandigital(number):
    digits = list(str(number))

    for i in range(1, 10):
        if secondStep(digits, i) == False:
            return False
        

 



j = 0
for i in range(987654321, 123456789, -2):
    j+=1
    if checkPandigital(i):
        if auxiliarFunctions.isPrimeForEx41(i):
            print("Prime: " + str(i))
    if j >= 1000000:
        print(i)
        j = 0
'''

#40
'''
strAux = ""
for i in range(190000):
    strAux += str(i)


result = int(strAux[1]) * int(strAux[10]) * int(strAux[100]) * int(strAux[1000]) * int(strAux[10000]) * int(strAux[100000]) * int(strAux[1000000])
print(result)

'''


#39
'''

def checkAngle(A, B, C):
    print("Sides: A:"+str(A)+"; B:"+str(B)+"; C:"+str(C)+";")
    angle = math.degrees(math.acos((pow(A, 2) + pow(B, 2) - pow(C, 2)) / (2 * A * B)))
    print(angle)
    return angle


bestMatch = 0
bestCount = 0

for i in range(800, 850):
    count = 0
    print("Perimeter: " + str(i))
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
        print(str(bestMatch) + " - counts: " + str(bestCount))

print(str(bestMatch) + " - counts: " + str(bestCount))

'''


#38

'''
def sortAndCheckNumber(string):
    sortedStr = sorted(string)
    for k in range(9):
        if sortedStr[k] != str(k+1):
            return False
    return True



bestMatch = 0
bestPandigital = 0

for n in range(2, 10):
    for i in range(1, 800000):
        auxStr = ""
        #print('Result for' , i , ' and (', end='')
        for j in range(1, n+1):
            #print(j , ',', end='')
            #print("multiplying " + i + " * " + n)
            auxStr += str(i * j)
        if len(auxStr) > 9:
            #print(') - result:',auxStr)
            break
        elif len(auxStr) < 9:
            continue
        else:
            if sortAndCheckNumber(auxStr) and int(auxStr) > bestPandigital:
                bestPandigital = int(auxStr)
                bestMatch = i

print("pandigital: " + str(bestPandigital) + "; match: " + str(bestMatch))

            
        
        #print(') - result:',auxStr)
        
'''


#37 - funciona mas é mt lento, nao consigo chegar a resultado

'''
def removeRightDigit(digits):
    for i in range(len(digits)-1):
        digits = digits[:-1]
        if int(digits) == 1:
            return False
        if auxiliarFunctions.isPrime(int(digits)) == False:
            return False

    return True

def removeLeftDigit(digits):
    for i in range(len(digits)-1):
        digits = digits[1:]
        if int(digits) == 1:
            return False
        if auxiliarFunctions.isPrime(int(digits)) == False:
            return False

    return True
 

sum = 0
count = 0
for i in range(10, 100000):
    if not auxiliarFunctions.isPrime(i):
        continue
        
    digits = str(i)

    if digits[0] == '1' or digits[len(digits)-1] == '1':
        #print("Passed " + str(i) + " because has 1 in beg or end")
        continue

    if int(digits[0]) % 2 == 0 or int(digits[len(digits)-1]) % 2 == 0:
        continue

    if removeRightDigit(str(i)) and removeLeftDigit(str(i)):
        sum += i
        count += 1        
        print("Adding " + str(i) + " to the sum ("+str(sum)+") and count("+str(count)+")")

    if count == 11:
        break

print(sum)



'''




#36
'''
def DecimalToBinary(num):
    aux = list(bin(num))
    aux = aux[2:len(aux)]
    return aux


def isPalindromic(digits):
    
    #print(digits)
    length = len(digits)
    #print("len: "+ str(length))
    for i in range(length // 2):
        #print(str(i) + ": " + str(digits[i]) + " - " + str(digits[length - i - 1]))
        if not digits[i] == digits[length - i - 1]:
            return False

    return True


sum = 0

for i in range(1000000):
    array = []
    digits = list(str(i))
    digitsBin = DecimalToBinary(i)#DecimalToBinary(i, array)


    #print(str(digits) + " - " + str(digitsBin))
    if isPalindromic(digits) and isPalindromic(digitsBin):
        sum += i

print("Sum: " + str(sum))


'''
##35

'''
def rotateDigits(digits, length):

    aux = []
    for i in range(1, length):
        aux.append(digits[i])
    aux.append(digits[0])
    #print(aux)

    return aux

def digitsArrayToInt(digits, length):
    strTest = ""
    for i in range(length):
        strTest += digits[i]
    
    #print(strTest)
    return int(strTest)



def checkRotations(number):
    digits = list(str(number))

    length = len(digits)
    if length == 1:
        return True

    for i in range(length-1):
        #print("rotation #" + str(i+1))
        digits = rotateDigits(digits, length)
        rotation = digitsArrayToInt(digits, length)
        if auxiliarFunctions.isPrime(rotation) == False:
            return False

    return True
#print(auxiliarFunctions.isPrime(791))

count = 1
print("Added 2 to count - "+str(count))


for i in range(2, 1000000):
    
    if auxiliarFunctions.isPrime(i) == False:
        continue

    #print("\nNumber: " + str(i))

    if checkRotations(i) == False:
        continue

    count += 1
    print("Added " + str(i) + " to count - "+str(count))

print(count)

'''


##34 - ta a fazer bem mas so encontra o 145
'''

def calcFactorial(number):
    total = number
    for i in range(number-1, 0, -1):
        total = total * i
    return total



for i in range(11, 100000000):
    sumTotal = 0
    for digit in str(i):
        sumTotal += calcFactorial(int(digit))
    if sumTotal == i:
        print(str(i) + ": " + str(sumTotal))
        print("^^^^^^^^^^^^^^^^^^^^")
'''

##32
'''
def twoEqualDigits(number):
    array = [int(i) for i in str(number)]
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return True

def shareDigit(multiplicand, multiplier):
    for digitMultiplicand in str(multiplicand):
        for digitMultiplier in str(multiplier):
            if digitMultiplicand == digitMultiplier:
                return True

def checkPandigital(multiplicand, multiplier, product):
    array = [int(i) for i in str(multiplicand)]
    array += [int(i) for i in str(multiplier)]
    array += [int(i) for i in str(product)]

    if len(array) != 9:
        return False

    for d in array:
        if d == 0:
            return False

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                return False

    print(array)
    return True



sum = []

for i in range(10000):
    for j in range(i+1, 10000):
        multiplicand = i
        multiplier = j
        product = i * j

        if twoEqualDigits(multiplicand) or twoEqualDigits(multiplier) or twoEqualDigits(product):
            continue
        
        if checkPandigital(multiplicand, multiplier, product):
            sum += [product] 
            print(str(i) + " * "+str(j)+" = "+str(product))


positions = []
for i in range(len(sum)):
    for j in range(i+1, len(sum)):
        if sum[i] == sum[j]:
            positions += [j]

for position in positions:
    sum.pop(position)

print(sum)
finalSum = 0
for number in sum:
    finalSum += number

print(finalSum)

'''
        



##31
'''
totalWays = 0

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

collection = CoinCollection(0, 0, 0, 0, 0, 0, 0, 0)
node = Node(0, 0, 0, 0, 0, 0, 0, 0)

print(totalWays)
'''

##30
'''
power = 5
finalSum = 0


for i in range(2, 10000000):
    testStr = ""
    sum = 0
    for d in str(i):
        testStr += str(d) + "^" + str(power) + " + " 
        sum += int(d) ** power
    testStr += "= "+str(sum)
    if sum == i: 
        finalSum += i
        print(testStr)


print(finalSum)
'''


##18 
'''
##f = open("treeNumbers.txt", "r")
f = open("treeNumbers2.txt", "r")
j = 1
numbers = []
for line in f:
    numbers.append(line.split())
    
arvore = Tree(numbers)
##arvore.getRightNodeValuesSummed()
arvore.getBiggerValue()
'''






''' #17
totalString = ""

for i in range(1, 1000):
    add = auxiliarFunctions.startWritingNumber(str(i))
    print(add)
    totalString += add

totalString+="onethousand"
print(len(totalString))
'''



'''#16
num = 2
for i in range(999):
    num = num * 2

numStr = str(num)
print(len(numStr))

result = int(numStr[0])
for j in range(1, len(numStr)):
    print('result is:', result,'; adding:', numStr[j])
    result = result + int(numStr[j])

print(result)

'''

'''##15
n = 20
aux = n + 1
biarray = [[0 for x in range(aux)] for y in range(aux)] 

biarray[n-1][n] = 1 
biarray[n][n-1] = 1 

for i in range(2, (n*2)+1):
    for j in range(i+1):
        if (n-j) == 20:
            biarray[n-i+j][n-j] = biarray[n-i+j+1][n-j]
        elif(n-i+j) == 20:
            biarray[n-i+j][n-j] = biarray[n-i+j][n-j+1]
        else:
            biarray[n-i+j][n-j] = biarray[n-i+j+1][n-j] + biarray[n-i+j][n-j+1]

for k in range(n+1):
    print(k, '-\t',biarray[k])

print('\nresult:',biarray[0][0])
'''

''' ##14
train = 0
number = 0

for i in range (2,1000001):
    n = i
    aux = 0
    while 1:
        if(n % 2) == 0:
            n = n / 2
        else:
            n = (n*3) + 1

        ##print(i,' - ', n)

        aux += 1
        if n == 1:
            if train < aux:
                train = aux
                number = i
            break

print(number,' - ',train)
'''

'''#13
f = open("100_50digit.txt", "r")
firstten = []
sum = 0
for i in range (100):
    number = f.readline()
    sum += int(number)
print(sum)
'''

'''##12 FODIDISSIMO
start_time = time.time()
triangleNumber = 0
aux = 1
maxDivisors = 0
while 1:
    while 1:
        triangleNumber += aux
        aux += 1
        if(triangleNumber % 2 ) == 0:
            break
    divisors = auxiliarFunctions.getDivisors(triangleNumber)
    if divisors > maxDivisors:
        maxDivisors = divisors
        print(triangleNumber, ': ',maxDivisors)
    
    if divisors > 500:
        print(triangleNumber,'[',divisors,']:', divisors)
        break


print("--- %s seconds ---" % (time.time() - start_time))
'''

'''#11
grid =" \
08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08 \
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00 \
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65 \
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91 \
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 \
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50 \
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 \
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21 \
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 \
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95 \
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92 \
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57 \
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58 \
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40 \
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66 \
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69 \
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36 \
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16 \
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54 \
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48 "

numbers = grid.split()

gs = 20

biggestProduct = 0
lastI=0
lastJ=0
direction = 'hi'
diagonalLeftValue = 0

for i in range(gs):
    for j in range(gs):
        if j < gs - 3:
            horizontalValue = int(numbers[(i*gs) + j]) * int(numbers[(i*gs) + j + 1]) * int(numbers[(i*gs) + j + 2]) * int(numbers[(i*gs) + j + 3])
            ##print('numbers: ', numbers[(i*gs) + j],', ', numbers[(i*gs) + j + 1],', ', numbers[(i*gs) + j+2],', ', numbers[(i*gs) + j+3],'; horizontal product: ',horizontalValue)
        if i < gs - 3:
            verticalValue = int(numbers[(i*gs) + j]) * int(numbers[((i+1)*gs) + j]) * int(numbers[((i+2)*gs) + j]) * int(numbers[((i+3)*gs) + j])
            ##print('numbers: ', numbers[(i*gs) + j],', ', numbers[((i+1)*gs) + j],', ', numbers[((i+2)*gs) + j],', ', numbers[((i+3)*gs) + j],'; vertical product: ',verticalValue)
        if i < gs - 3 and j < gs - 3:
            diagonalRightValue = int(numbers[(i*gs) + j]) * int(numbers[((i+1)*gs) + j + 1]) * int(numbers[((i+2)*gs) + j + 2]) * int(numbers[((i+3)*gs) + j + 3])
            ##print('numbers: ', numbers[(i*gs) + j],', ', numbers[((i+1)*gs) + j + 1],', ', numbers[((i+2)*gs) + j + 2],', ', numbers[((i+3)*gs) + j + 3],'; diagonal right product: ',diagonalRightValue)
        if i < gs - 3 and j > 2:
            diagonalLeftValue = int(numbers[(i*gs) + j]) * int(numbers[((i+1)*gs) + j - 1]) * int(numbers[((i+2)*gs) + j - 2]) * int(numbers[((i+3)*gs) + j - 3])
            ##print('numbers: ', numbers[(i*gs) + j],', ', numbers[((i+1)*gs) + j - 1],', ', numbers[((i+2)*gs) + j - 2],', ', numbers[((i+3)*gs) + j - 3],'; diagonal left product: ',diagonalLeftValue)
        
        
        if biggestProduct < horizontalValue:
                biggestProduct = horizontalValue
                lastI = i
                lastJ = j
                direction = 'Horizontal'
        if biggestProduct < verticalValue:
                biggestProduct = verticalValue
                lastI = i
                lastJ = j
                direction = 'Vertical'
        if biggestProduct < diagonalRightValue:
                biggestProduct = diagonalRightValue
                lastI = i
                lastJ = j
                direction = 'Diagonal Right'
        if biggestProduct < diagonalLeftValue:
                biggestProduct = diagonalLeftValue
                lastI = i
                lastJ = j
                direction = 'Diagonal Left'
print(biggestProduct, '; in position [',lastI+1,',',lastJ+1,'] in ',direction)
'''

'''##10 - tive que ir ver a net, que formula mais f*****
start_time = time.time()
n = 2000000

sum = 0
array = [True] * n


for p in range(2, n):
    if array[p]:
        sum += p
        for i in range(p*p, n, p):
            array[i] = False
print(sum)


print("--- %s seconds ---" % (time.time() - start_time))
'''


'''#9
found = False

for c in range(999):
    if(found):
        break
    for b in range(999):
        if(b >= c) or found:
            break
        for a in range(999):
            if(a >= b) or found:
                break
            if((a*a)+(b*b) == (c*c)) and a+b+c == 1000:
                print(a, ' - ',b,' - ',c)
                product = a*b*c
                print(product)
                found = True
'''

'''#8
num = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
numArray = [int(x) for x in str(num)] 
print(num)
print(numArray)

greatestProduct = 0
position = 0

auxArray = []
for i in range(0, 1000-13):
    aux = 1
    for j in range (0, 13):
        auxArray.append(numArray[i+j])
        aux = aux * numArray[i+j]
    if()
    print((i+1), ' - ', auxArray, '; total = ',aux)
    if(aux > greatestProduct ):
        greatestProduct = aux
        position = i+1
    auxArray.clear()

print(position, ' - ',greatestProduct)
'''

'''#7
prime = 0
for i in range(10001):
    prime = auxiliarFunctions.getNextPrimeNumber(prime)
    print((i+1), ' - ', prime)
'''

'''#6
squareOfSums = 0
sumSquares = 0
for i in range(1, 101):
    sumSquares += (i * i)
    squareOfSums += i

squareOfSums = squareOfSums * squareOfSums

result = squareOfSums - sumSquares
print(result)
'''

'''#5
smallestNum = 0
i = 20
while 1:
    for j in range (2, 21):
        if (i % j) != 0:
            break
        if(j == 20):
            smallestNum = i
    if(smallestNum != 0):
        break
    i+=1
print(smallestNum)
'''

'''#4
bigger = 0
for i in range(999, 99, -1):
    for j in range(999, 99, -1):
        num = i * j
        res = [int(x) for x in str(num)] 
        ##print(res[len(res)-1])
        if res[0] == res[len(res)-1] and res[1] == res[len(res)-2] and res[2] == res[len(res)-3]:
            ##print('i: ',i,';  j: ',j, ';  num: ',num)
            if(num > bigger):
                bigger = num

print(bigger)
'''

'''#3


prime_factors = []
prime = 2
wat = 600851475143

while(wat != 0):
    if (wat % prime) == 0:
        wat = wat / prime
        prime_factors.append(prime)

        print('found a prime factor: ',prime,';   wat is now: ',wat)

        prime = 2
    else:
        prime = getNextPrimeNumber(prime)

'''




'''#2
prevRes = 1
result = 2
final_result = 2

even_numbers = []

for i in range(1, 40):
    aux = result + prevRes
    print('aux: ',aux)
    if aux > 4000000:
        print('broke with aux: ',aux)
        break

    prevRes = result
    result = aux

    if(result % 2) == 0:
        final_result += result


print(final_result)
'''





''' #1
result = 0
for x in range(1000):
    if (x % 3) == 0 or (x % 5) == 0 :
        result += x
print(result)
'''


