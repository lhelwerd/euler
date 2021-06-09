"""
PROBLEM:     170
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Largest pandigital number (including 0 through 9 once) that is the
    concatenation of two numbers a and b which share a proper divisor n,
    where the concatenation of n, a / n and b / n is also a pandigital number
"""

from itertools import permutations
import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(10 ** 6)
    digits = list("0123456789")
    for product in permutations(reversed(digits)):
        if product[0] == '0':
            continue
        for i in range(3, 7):
            a = int(''.join(product[:i]))
            b = int(''.join(product[i:]))
            for div in primes.proper_divisors(a):
                if b % div == 0 and sorted(str(div) + str(a // div) + str(b // div)) == digits:
                    print(''.join(product))
                    return

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
