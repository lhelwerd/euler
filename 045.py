"""
PROBLEM:     045
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Smallest triangular number greater than 40755 that is also pentagonal and
    hexagonal.
    Triangular: T_n = n(n+1)/2
    Pentagonal: P_n = n(3n-1)/2
    Hexagonal:  H_n = n(2n-1)
"""

import math
import timeit
from Euler.formula import FormulaSet

def problem():
    triangular = lambda n: n * (n + 1) / 2
    pentagonal = FormulaSet(lambda n: n * (3 * n - 1) / 2,
                            lambda num: ((math.sqrt(24 * num + 1) + 1) / 6),
                            1)
    hexagonal = FormulaSet(lambda n: n * (2 * n - 1),
                           lambda num: ((math.sqrt(8 * num + 1) + 1) / 4),
                           1)

    n = 286
    t = triangular(n)
    while t not in pentagonal or t not in hexagonal:
        n += 1
        t = triangular(n)

    print(t)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

