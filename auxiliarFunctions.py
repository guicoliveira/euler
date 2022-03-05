import math

def digitsArrayToInt(digits, length):
    
    return int(digits)

    '''strTest = ""
    for i in range(length):
        strTest += digits[i]
    
    #print(strTest)
    return int(strTest)'''


def isPrimeForEx41(number):
    for i in range(3, int(number/2)+1, 2):
        if(number % i) == 0:
            return False

    return True

def is_prime(n: int) -> bool:
    """Got it from the internet. Primality test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def isPrime(number):
    """Don't use this one, use the newer is_prime()"""
    if(number % 2) == 0:
        return False
    for i in range(3, int(number/3), 2):
        if(number % i) == 0:
            return False

    return True

def getNextPrimeNumber(startingNumber):
    if startingNumber % 2 == 0:
        startingNumber += 1
    else:
        startingNumber += 2
    
    while True:
        if is_prime(startingNumber):
            return startingNumber
        else:
            startingNumber += 2


def getDivisorsOld(number):
    ##divisors = []
    ##divisors.append(1)
    nDiv = 1
    for i in range(2, int((number/4))):
            if(number % i) == 0:
                print(number, ' is divisivel por ', i)
                nDiv += 1##divisors.append(i)

    return nDiv*2


def getDivisors(number):
    nDiv = 1 ## 1 
    for i in range(2, int(math.sqrt(number))+1):
        if (number % i) == 0:
            ##print('for ', number, ' divisors: ', i)
            nDiv += 1
    nDiv = nDiv * 2 

    ##print('sqrt: ',int(math.sqrt(number)))
    if(int(math.sqrt(number)) * int(math.sqrt(number)) == number):
        nDiv -= 1

    return nDiv

def startWritingNumber(number):
    if(len(number) == 3):
        return getThreeDigitNumberWritten(number)
    elif(len(number) == 2):
        return getTwoDigitNumberWritten(number)
    elif(len(number) == 1):
        return getOneDigitNumberWritten(number)

def getThreeDigitNumberWritten(number):
    switcher = {
        '0': "",
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine"
    }

    centena = switcher.get(number[0], "Invalid number")
    centena += "hundred"

    if(number[1] == '0' and number[2] == '0'):
        return centena
    else:
        centena += "and"

    dezena = number[1]
    dezena += number[2]
    centena += getTwoDigitNumberWritten(dezena)

    return centena


    
def getTwoDigitNumberWritten(number):
    switcher = {
        '0': "",
        '2': "twenty",
        '3': "thirty",
        '4': "forty",
        '5': "fifty",
        '6': "sixty",
        '7': "seventy",
        '8': "eighty",
        '9': "ninety"
    }

    if(number[0] == '1'):
        return getFrom10To20NumberWritten(number[1])

    dezena = switcher.get(number[0], "Invalid number")
    dezena += getOneDigitNumberWritten(number[1])

    return dezena

def getFrom10To20NumberWritten(number):
    switcher = {
        '0': "ten",
        '1': "eleven",
        '2': "twelve",
        '3': "thirteen",
        '4': "fourteen",
        '5': "fifteen",
        '6': "sixteen",
        '7': "seventeen",
        '8': "eighteen",
        '9': "nineteen"
    }
    return (switcher.get(number, "Invalid month"))


def getOneDigitNumberWritten(number):
    switcher = {
        '0': "",
        '1': "one",
        '2': "two",
        '3': "three",
        '4': "four",
        '5': "five",
        '6': "six",
        '7': "seven",
        '8': "eight",
        '9': "nine"
    }
    return (switcher.get(number, "Invalid month"))