"""
PROBLEM:     023
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of the numbers that cannot be written as a sum of two abundant numbers,
    which have a sum of proper divisors greater than themselves.
"""

from builtins import range
from itertools import combinations_with_replacement
import timeit
from Euler.divisor import proper_divisors

def problem():
    abundant = set()
    limit = 28123
    for n in range(2, limit + 1):
        divisors = proper_divisors(n)
        divisor_sum = sum(divisors)
        if divisor_sum > n:
            abundant.add(n)

    two_abundant = set(x + y for (x, y) in combinations_with_replacement(abundant, 2) if x + y <= limit)
    print(sum(m for m in range(1, limit + 1) if m not in two_abundant))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

