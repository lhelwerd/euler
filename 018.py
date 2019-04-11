"""
PROBLEM:     018
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Maximum triangle path sum (small)
"""

import timeit
from Euler.triangle import path

def problem():
    print(path('018.txt'))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

