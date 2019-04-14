"""
PROBLEM:     003
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Largest prime factor of a large number.
"""

import math
import timeit
from Euler.prime import PrimeSet

def problem():
    n = 600851475143
    primes = sorted(PrimeSet(int(math.sqrt(n))))
    for x in reversed(primes):
        if n % x == 0:
            print(x)
            break

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

