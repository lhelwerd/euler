"""
PROBLEM:     052
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Smallest number x > 0 where 2x, 3x, 4x, 5x and 6x contain the same digits.
"""

import timeit

def problem():
    x = 1
    limit = 10
    digits = ['1']
    while any(digits != sorted(str(i * x)) for i in range(2, 7)):
        if 6 * x < limit:
            x += 1
        else:
            while 6 * x >= limit:
                x = limit
                limit *= 10

        digits = sorted(str(x))

    print(x)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
