"""
PROBLEM:     073
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of reduced proper fractions with denominator at most 12000 that are
    between 1/3 and 1/2.
"""

from past.builtins import xrange as range
from math import ceil
import timeit
from Euler.prime import PrimeSet

def problem():
    limit = 12000
    primes = PrimeSet(limit)
    divisors = [set([0]), set([1])]
    count = 0
    for d in range(2, limit + 1):
        if d in primes:
            divisors.append(set([d]))
        else:
            divisors.append(set(primes.factorize(d).keys()))

        for n in range(max(2, int(ceil(d / 3.))), int(ceil(d / 2.))):
            if divisors[n].isdisjoint(divisors[d]):
                count += 1

    print(count)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
