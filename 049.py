"""
PROBLEM:     049
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Concatenation of three 4-digit prime numbers a < b < c where b - a = c - b
    and each number is a permutation of another, other than 1487, 4817, 8147.
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(10000, extendable=False)
    for a in primes:
        if a > 999 and a != 1487:
            digits = set(str(a))
            for b in primes:
                if b > a:
                    c = b + b - a
                    if c < 10000 and c in primes and set(str(b)) == digits and set(str(c)) == digits:
                        print(str(a) + str(b) + str(c))
                        return

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
