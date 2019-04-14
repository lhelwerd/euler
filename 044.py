"""
PROBLEM:     044
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3
EXPLANATION:
    Pair of pentagonal numbers with smallest difference whose sum and difference
    are both pentagonal.
"""

import math
import timeit
from Euler.formula import FormulaSet

def problem():
    pentagonal = FormulaSet(lambda n: n * (3 * n - 1) / 2,
                            lambda num: ((math.sqrt(24 * num + 1) + 1) / 6),
                            10000)

    smallest = float('inf')
    numbers = list(sorted(pentagonal.numbers))
    for i, j in enumerate(numbers):
        for k in numbers[i+1:]:
            d = abs(j - k)
            if d < smallest and d in pentagonal and j + k in pentagonal:
                smallest = d

    print(smallest)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

