"""
PROBLEM:     123
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Least value of n for which (p_n-1)^n + (p_n+1)^n has a remainder of over
    10^10 when divided by p_n^2, where p_n is the nth prime.
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(10**6)
    target = 10**10
    start = 7037
    for i, p in enumerate(primes[start:]):
        p_squared = p * p
        n = start + i + 1
        v = (pow(p - 1, n, p_squared) + pow(p + 1, n, p_squared)) % p_squared
        if v > target:
            break

    print(n)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

