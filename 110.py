"""
PROBLEM:     110
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    The least value of n for which the number of solutions for 1/x + 1/y = 1/n
    exceeds four million.
"""

import timeit
from Euler.prime import PrimeSet
from itertools import combinations_with_replacement

def problem():
    target = 4*10**6
    # Only try low prime numbers, do not consider factorizations where a higher 
    # prime number has a higher exponent than a previous one (reversed), and 
    # limit exponents to 3 max
    primes = PrimeSet(40)
    options = combinations_with_replacement(range(4), len(primes))
    best = float('Inf')
    best_p = {}

    for factors in options:
        p = dict(zip(primes, reversed(factors)))
        # Number of distinct solutions is (tau(n^2) + 1) / 2
        divisors = 1
        for factor, exp in p.items():
            # Since we want to know the divisors of the square, multiply each 
            # factor's exponent with 2.
            divisors *= (exp * 2 + 1)

        solutions = (divisors + 1) // 2
        if solutions > target and solutions < best:
            best = solutions
            best_p = p

    n = 1
    for factor, exp in best_p.items():
        n *= factor ** exp
    print(n)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

