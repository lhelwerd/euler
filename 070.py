"""
PROBLEM:     070
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3
EXPLANATION:
    Value of n below one million for which n/phi(n) is maximal.
"""

from past.builtins import xrange as range
import timeit
from Euler.prime import PrimeSet

def problem():
    limit = 10**7
    primes = PrimeSet(limit)
    phis = [0, 1]
    best = float('inf')
    best_n = 0
    for n in range(2, limit + 1):
        phi = primes.totient(n, phis)
        if n / phi < best and sorted(str(n)) == sorted(str(int(phi))):
            best_n = n
            best = n / phi

    print(best_n)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
