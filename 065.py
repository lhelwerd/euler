"""
PROBLEM:     065
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of digits of the numerator of the 100th convergent in the continued
    fraction expansion of e.
"""

from past.builtins import xrange as range
from decimal import Decimal
import timeit
from Euler.fraction import expand

def problem():
    x1 = 1
    y1 = 0
    x2 = 2
    y2 = 1
    i = 1
    limit = 100
    while i < limit:
        x1, x2 = x2, x2 * (2 * (i + 1) // 3) + x1 if i % 3 == 2 else x2 + x1
        y1, y2 = y2, y2 * (2 * (i + 1) // 3) + y1 if i % 3 == 2 else y2 + y1
        i += 1

    print(sum(int(d) for d in str(x2)))

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
