import math

def find_sqrt(n):
    return math.sqrt(n)


def find_ceil(n):
    return math.ceil(n)

def divisors(num: int) -> list:
    divisors_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors_list.append(i)
    return divisors_list
