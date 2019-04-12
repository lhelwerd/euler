"""
PROBLEM:     025
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Index of the first term in the Fibonacci sequence with 1000 digits
"""

import math
import timeit

def problem():
    first = 1
    second = 1
    i = 2
    bound = 10 ** 999
    while second < bound:
        first, second = second, first + second
        i += 1

    print(i)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
