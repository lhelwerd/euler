"""
PROBLEM:     035
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of prime numbers whose digit permutations are themselves prime
"""

from itertools import permutations
import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(int(1e6))
    circular = set()
    for prime in primes:
        digits = str(prime)
        test = digits[1:] + digits[0]
        while test != digits and int(test) in primes:
            test = test[1:] + test[0]
        if test == digits:
            circular.add(prime)

    print(len(circular))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
