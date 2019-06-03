"""
PROBLEM:     112
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Least number at which the proportion of numbers that are neighter increasing
    nor decreasing is exactly 99%.
"""

import timeit

def is_bouncy(n):
    increasing = True
    decreasing = True
    prev = n % 10
    n //= 10
    while (increasing or decreasing) and n > 0:
        if n % 10 > prev:
            decreasing = False
        if n % 10 < prev:
            increasing = False
        prev = n % 10
        n //= 10

    return not (increasing or decreasing)

def problem():
    n = 100
    bouncy = 0 # 100 is decreasing
    target_numerator = 99
    target_denominator = 100
    while bouncy * target_denominator < target_numerator * n:
        n += 1
        bouncy += is_bouncy(n)

    print(n)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
