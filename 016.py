"""
PROBLEM:     016
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of the digits of 2^1000
"""

import math
import timeit

def problem():
    print(sum(int(d) for d in str(2**1000)))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
