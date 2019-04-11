"""
PROBLEM:     067
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Maximum triangle path sum (large)
"""

import timeit
from Euler.triangle import path

def problem():
    print(path('p067_triangle.txt'))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
