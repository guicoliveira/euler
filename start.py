import time
from auxiliarClasses.Tree import *
import auxiliar_functions
import sys
import glob
from exercises import *
import exercises


exercise_number = None
try:
    exercise_number = int(sys.argv[1])
except ValueError:
    print("First argument must be the number of the exercise.")
    exit()
except IndexError:
    print("Need to choose the exercise number as the first argument. Ex: py start.py 22")
    exit()

if not exercise_number:
    print("Exercise number is not defined")
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


'''#9

'''

'''#8

'''

'''#7

'''

'''#6

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


