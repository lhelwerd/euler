"""
PROBLEM:     134
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of the smallest numbers that end in the digits of prime numbers p1
    (between 5 and one million) and are multiples of each next prime p2.
"""

import math
import timeit
from Euler.prime import PrimeSet
from Euler.modulo import inverse

def problem():
    limit = 1000003
    primes = PrimeSet(limit)
    pi = iter(primes)
    # Skip 2 and 3
    next(pi)
    next(pi)
    p1 = next(pi) # 5
    total = 0
    for p2 in pi:
        step = 10 ** math.ceil(math.log10(p1))
        x = p1 * p2 * inverse(p2, step) % (p2 * step)

        total += x
        p1 = p2

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
