"""
PROBLEM:     005
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3
EXPLANATION:
    Smallest number that is divisible with no remainder by numbers 1 through 20
"""

from builtins import range
import timeit
import math

def problem():
    limit = math.factorial(20)
    check = tuple(range(20, 10, -1))
    for i in range(20, limit):
        for j in check:
            if i % j != 0:
                break
        else:
            print(i)
            break

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

