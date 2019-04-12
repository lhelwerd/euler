"""
PROBLEM:     027
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Product of the coefficients of the quadratic formula n^2 + an + b that
    generates the most primes for consecutive values of n = 0, ..., m with
    |a| < 1000 and |b| <= 1000.
"""

from builtins import range
import timeit
from Euler import Sieve

def problem():
    primes = Sieve(int(2e6))

    best_coeff = 0
    best = 0

    for a in range(-1000 + 1, 1000):
        for b in range(-1000, 1000 + 1):
            n = 0
            while n ** 2 + a * n + b in primes:
                n += 1

            if n > best:
                best = n
                best_coeff = a * b

    print(best_coeff)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

