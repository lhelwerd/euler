"""
PROBLEM:     034
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of numbers that are equal to the sum of factorials of their digits.
"""

from builtins import range
import math
import timeit

def problem():
    cache = tuple(math.factorial(n) for n in range(10))
    limit = 50000 # https://oeis.org/A014080
    total = 0
    for i in range(10, limit):
        if i == sum(cache[int(d)] for d in str(i)):
            total += i

    print(total)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
