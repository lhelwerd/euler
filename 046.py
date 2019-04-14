"""
PROBLEM:     046
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Smallest odd non-prime number that cannot be expressed as the sum of
    a prime number plus two times a square number.
"""

from builtins import range
import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(10**3)
    i = 35
    double_squares = [2 * x ** 2 for x in range(1, 55)]
    while i in primes or any(i - s in primes for s in double_squares if s < i):
        i += 2

    print(i)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
