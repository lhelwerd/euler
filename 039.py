"""
PROBLEM:     039
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Perimeter (sum of sides) value that has the maximum number of different
    right angle triangles with {a,b,c} (so where a**2 + b**2 = c**2)
"""

from builtins import range
import math
import timeit

def problem():
    solutions = [0] * 1001
    for a in range(1, 1000):
        # a + b + c <= 1000
        # b >= a to avoid symmetry
        # c = sqrt(a**2 + b**2) >= sqrt(a**2 + a**2) = sqrt(2) * a
        for b in range(a, 1000 - a - math.sqrt(2) * a):
            c = math.sqrt(a**2 + b**2)
            p = a + b + c
            if p == int(p) and p <= 1000:
                solutions[int(p)] += 1

    print(solutions.index(max(solutions)))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
