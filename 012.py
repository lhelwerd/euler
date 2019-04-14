"""
PROBLEM:     012
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    First triangle number with over five hundred divisors
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(10**4)
    triangle = 0
    i = 1
    divisors = 0
    while divisors < 500:
        triangle += i
        divisors = 1

        # Perform a prime factorization and calculate the number of divisors 
        # according to https://math.stackexchange.com/a/1853205:
        # if n = p1^e1 * p2^e2 * ... * pr^er then the number of divisors is
        # (e1 + 1) * (e2 + 1) * ... * (er + 1).
        factors = primes.factorize(triangle)
        for factor in factors.itervalues():
            divisors *= factor + 1

        i += 1

    print(triangle)


if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
