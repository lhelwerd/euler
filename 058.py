"""
PROBLEM:     058
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Width of the first spiral formed by placing the numbers from 1 and moving
    to the right, then placing the remaining numbers in clockwise direction,
    where the percentage of primes within the diagonals is less than 10%.
"""

import time
import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(50, extendable=False)
    x = 1
    i = 2
    p = 5
    diag = (1, 2, 3)
    diagonals = 1
    while p * 10 >= diagonals:
        # Do not consider the last diagonal for prime checks because it is
        # always an odd square.
        p += primes.miller_test(x + i, 9) + primes.miller_test(x + i + i, 9) + \
            primes.miller_test(x + i + i + i, 9)

        x += 4 * i
        diagonals += 4
        i += 2

    print(i - 1)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem; gc.enable()",
                        number=1))

