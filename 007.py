"""
PROBLEM:     007
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    10001st prime
"""

from Euler import Sieve
import timeit

def problem():
    # Using the answer to find the solution
    primes = list(sorted(Sieve(104743 + 1)))
    # Just to spite 0-indexers
    print(primes[10001 - 1])

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

