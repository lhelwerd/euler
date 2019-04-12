"""
PROBLEM:     028
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of diagonals of a 1001 x 1001 spiral formed by placing the numbers
    from 1 and moving to the right, then placing the remaining numbers in
    clockwise direction (1001^2 in total).
"""

from builtins import range
import timeit

def problem():
    total = 1
    x = 1
    size = 1001
    for i in range(3, size + 1, 2):
        for _ in range(4):
            x += i - 1
            total += x

    print(total)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

