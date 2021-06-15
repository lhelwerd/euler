"""
PROBLEM:     146
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3
EXPLANATION:
    Numbers n below 150 million where n**2+1, n**2+3, n**2+7, n**2+9,
    n**2+13, and n**2+27 are consecutive primes
"""

import timeit
from Euler.prime import PrimeSet

def go(primes, start, limit, a):
    total = 0
    good = (1, 3, 7, 9, 13, 27)
    for n in range(start, limit):
        n_sq = n * n
        # Only n**2+21 is ever a prime that could break consecutiveness (in 
        # this range at least)
        if all(primes.miller_test(n_sq + i, a) for i in good) and \
            not primes.miller_test(n_sq + 21, a):
            total += n

    return total

def problem():
    primes = PrimeSet(25, extendable=False)
    limit = 150000000
    total = 0
    total += go(primes, 10, 1172, 2)
    total += go(primes, 1172, 5032, 3)
    total += go(primes, 5032, 56701, 4)
    total += go(primes, 56701, 1467072, 5)
    total += go(primes, 1467072, 1864068, 6)
    total += go(primes, 1864068, 18481073, 7)
    total += go(primes, 18481073, limit, 9)
    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
