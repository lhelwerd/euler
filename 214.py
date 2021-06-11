"""
PROBLEM:     214
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of primes below 40 million whose phi (totient number) recursively end
    up in a chain of length 25.
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(4 * 10 ** 7)
    limit = primes[-1]
    phis = [0, 1]
    lengths = [0] * (limit + 1)
    lengths[1] = 1
    total = 0
    for n in range(2, limit + 1):
        phi = primes.totient(n, phis)
        lengths[n] = lengths[phi] + 1
        if n in primes and lengths[n] == 25:
            total += n

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
