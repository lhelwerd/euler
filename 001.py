"""
PROBLEM:     001
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3 
EXPLANATION:
    Sum of all multiples of 3 or 5 below 1000.
"""

import math
import timeit

def sum(scalar, n):
    divided = math.ceil(n / float(scalar)) - 1
    return scalar * ((divided * (divided + 1)) / 2)

def problem():
    print(int(sum(3, 1000) + sum(5, 1000) - sum(15, 1000)))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1) / 1)
