"""
PROBLEM:     064
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of continued fractions of n <= 10000 that have an odd period when
    expanding the fraction.
"""

from past.builtins import xrange as range
from decimal import Decimal
import timeit
from Euler.continued_fraction import expand_sqrt

def problem():
    odd = 0
    limit = 10000
    for n in range(1, limit + 1):
        expansion = list(expand_sqrt(n))
        if len(expansion) % 2 != 0:
            odd += 1

    print(odd)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
