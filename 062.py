"""
PROBLEM:     062
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Smallest cube for which exactly five permutations of its digits are cube.
"""

from itertools import permutations
from numpy import cbrt
import timeit
from Euler.formula import FormulaSet

def cube_perms(digits, length, formula):
    for p in formula:
        c = str(p)
        if len(c) > length:
            break
        if len(c) == length and sorted(c) == digits:
            yield p

def problem():
    formula = FormulaSet(lambda n: n * n * n,
                         lambda num: int(round(num ** (1/3.))),
                         5027)

    seen = set()
    for i, cube in enumerate(formula):
        if cube not in seen:
            digits = sorted(str(cube))
            cubes = set(cube_perms(digits, len(digits), formula))
            seen.update(cubes)
            if len(cubes) == 5:
                break

    print(cube)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
