"""
PROBLEM:     719
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of all square numbers whose root can be obtained from a sum of some
    splitting (with 2 or more numbers) of the decimals of the square number.
"""

import math
import timeit

def split(target, num):
    if target == num:
        return True
    if num < target and num < 10:
        return False
    place = 1
    for _ in range(1, int(math.ceil(math.log10(num)))):
        place *= 10
        x = num // place
        y = target - (num % place)
        if y <= 0:
            break
        if split(y, x):
            return True

    return False

def problem():
    limit = 10 ** 12
    total = 0
    # Skip 0**2 and 1**2 because they cannot be split into 2 or more numbers
    for i in range(2, int(limit ** 0.5) + 1):
        if split(i, i ** 2):
            total += i ** 2

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
