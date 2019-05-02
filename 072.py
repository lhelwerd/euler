"""
PROBLEM:     072
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of reduced proper fraction with denominator at most one million.
"""

from past.builtins import xrange as range
import timeit
from Euler.prime import PrimeSet

def problem():
    limit = 10**6
    primes = PrimeSet(limit)
    phis = [0, 1]
    for d in range(2, limit + 1):
        phi = primes.totient(d, phis)

    # Do not count 1/1
    print(sum(phis) - 1)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
