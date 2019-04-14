"""
PROBLEM:     041
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Largest prime number which contains all digits from 1 to n once, where
    n is the number of digits in the number.
"""

from builtins import range
from itertools import permutations
import timeit
from Euler.prime import PrimeSet

def problem():
    # Initialize a small set of primes to speed up divisor search for large 
    # potential primes
    primes = PrimeSet(10000)
    for n in range(9, 0, -1):
        for digits in permutations(range(n, 0, -1)):
            pan = int(''.join(str(d) for d in digits))
            if pan in primes:
                print(pan)
                return

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
