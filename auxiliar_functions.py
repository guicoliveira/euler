import math


def digits_array_to_int(digits, length):
    return int(digits)


def is_list_similar(li1, li2):
    return True if len(list(set(li1) - set(li2)) + list(set(li2) - set(li1))) == 0 else False


def is_odd_composite_number(number):
    if number % 2 == 0:
        return False

def is_prime_for_ex_41(number):
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


def get_next_prime_number(starting_number: int) -> int:
    if starting_number % 2 == 0:
        starting_number += 1
    else:
        starting_number += 2

    while True:
        if is_prime(starting_number):
            return starting_number
        else:
            starting_number += 2


def get_divisors(number):
    n_div = 1  ## 1
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            ##print('for ', number, ' divisors: ', i)
            n_div += 1
    n_div = n_div * 2

    ##print('sqrt: ',int(math.sqrt(number)))
    if (int(math.sqrt(number)) * int(math.sqrt(number)) == number):
        n_div -= 1

    return n_div


def start_writing_number(number):
    if (len(number) == 3):
        return get_three_digit_number_written(number)
    elif (len(number) == 2):
        return get_two_digit_number_written(number)
    elif (len(number) == 1):
        return get_one_digit_number_written(number)


def get_three_digit_number_written(number):
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

    if (number[1] == '0' and number[2] == '0'):
        return centena
    else:
        centena += "and"

    dezena = number[1]
    dezena += number[2]
    centena += get_two_digit_number_written(dezena)

    return centena


def get_two_digit_number_written(number):
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

    if (number[0] == '1'):
        return get_10_to_20_number_written(number[1])

    dezena = switcher.get(number[0], "Invalid number")
    dezena += get_one_digit_number_written(number[1])

    return dezena


def get_10_to_20_number_written(number):
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


def get_one_digit_number_written(number):
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
