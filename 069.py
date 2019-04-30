"""
PROBLEM:     069
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Value of n below one million for which n/phi(n) is maximal.
"""

from past.builtins import xrange as range
import timeit
from Euler.prime import PrimeSet

def problem():
    limit = 10**6
    primes = PrimeSet(limit)
    phis = [0, 1]
    best = 3.
    best_n = 6
    for n in range(2, limit + 1):
        phi = primes.totient(n, phis)
        if n / phi > best:
            best_n = n
            best = n / phi

    print(best_n)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
