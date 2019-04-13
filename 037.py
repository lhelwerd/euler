"""
PROBLEM:     037
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of all eleven primes that are truncatable from both left to right and
    right to left and still remain prime.
"""

import timeit
from Euler import Sieve

def problem():
    primes = Sieve(740000) # https://oeis.org/A020994
    truncatable = set()
    for prime in primes:
        digits = str(prime)
        length = len(digits)
        i = 1
        while i < length and int(digits[i:]) in primes and int(digits[:-i]) in primes:
            i += 1

        if length > 1 and i == length:
            truncatable.add(prime)

    print(sum(truncatable))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
