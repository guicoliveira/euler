import time
from auxiliarClasses.Tree import *
import auxiliarFunctions
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


