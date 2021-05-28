"""
PROBLEM:     127
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of all numbers c that have a pair (a, b) with a<b and a+b=c that have
    no common factors between a, b, and c and the product of the distinct
    factors is less than c
"""

import timeit
from Euler.prime import PrimeSet, CoprimeSet

def fast_factorize(primes, factors, n):
    if n not in factors:
        if n in primes:
            factors[n] = (n,)
        else:
            factors[n] = tuple(primes.factorize(n).keys())
    return factors[n]

def problem():
    limit = 120000
    primes = PrimeSet(limit)
    factors = {}
    total = 0
    for b, a in CoprimeSet(limit):
        c = a + b

        if a == 1:
            factors[a] = (1,)
        else:
            fast_factorize(primes, factors, a)

        fast_factorize(primes, factors, b)

        fast_factorize(primes, factors, c)

        prod = 1
        for f in factors[a]:
            prod *= f
        for f in factors[b]:
            prod *= f
        for f in factors[c]:
            prod *= f

        if prod < c:
            print(a, b, c)
            total += c

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
