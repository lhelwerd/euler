"""
PROBLEM:     179
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of each numbers n that has the same number of proper divisors as n + 1
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    limit = 10 ** 7
    primes = PrimeSet(limit)
    count = 0
    prev_divisors = 1 # n = 2 has two divisors 1, 2 but we do not count n
    for n1 in range(3, limit + 2):
        divisors = primes.proper_divisors(n1)
        if len(divisors) == prev_divisors:
            count += 1

        prev_divisors = len(divisors)

    print(count)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
