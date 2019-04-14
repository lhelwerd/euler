"""
PROBLEM:     010
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of primes below two million
"""

import timeit
from Euler import Sieve

def problem():
    primes = Sieve(int(2e6))
    print(sum(primes))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

