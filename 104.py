"""
PROBLEM:     104
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3
EXPLANATION:
    Index of first Fibonacci number whose first nine digits and last nine digits
    are pandigital
"""

import math
import timeit

def problem():
    first = 1
    second = 1
    k = 2
    pandigital = False
    pan = set(str(d) for d in range(1, 10))
    old = 0
    new = 0
    start = False
    end = ''
    while not (start and end):
        first, second = second, first + second
        k += 1

        new = second // (10 ** (int(math.log10(second)) - 8))
        if new != old:
            start = set(str(new)) == pan
            old = new
        end = set(str(second % (10 ** 9))) == pan

    print(k)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
