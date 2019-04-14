"""
PROBLEM:     047
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    First number of four consecutive numbers that have exactly four distinct
    prime factor.
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(10**4)

    consecutive = 0
    n = 210 # First number with four prime factors (2 * 3 * 5 * 7)
    while consecutive < 4:
        if len(primes.factorize(n)) == 4:
            consecutive += 1
        else:
            consecutive = 0

        n += 1

    print(n - 4)
        

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
