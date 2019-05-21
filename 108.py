"""
PROBLEM:     108
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    The least value of n for which the number of solutions for 1/x + 1/y = 1/n
    exceeds one thousand.
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    solutions = 0
    target = 1000
    n = 1
    primes = PrimeSet(10**6)
    while solutions <= target:
        n += 1
        if n not in primes and len(primes.factorize(n)) > 5:
            solutions = sum((n * x) % (x - n) == 0 for x in range(n+1,2*n+1))

    print(n)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

