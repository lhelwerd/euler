"""
PROBLEM:     071
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Numerator of the highest reduced proper fraction lower than 3/7 where
    the denominator is at most one million.

    Strategy:

    - For each d 2..1e6:
        - Find the first fraction n/d higher than the current highest generated
          reduced proper fraction, or 2/5 initially
        - Check if fraction is reduced via memoized divisors disjointness check
        - Stop generating if the fraction is higher than 3/7
"""

from past.builtins import xrange as range
from math import ceil
import timeit
from Euler.prime import PrimeSet

def problem():
    limit = 10**6
    primes = PrimeSet(limit)
    divisors = [set([0]), set([1])]
    best_num = 2
    best_den = 5
    for d in range(2, limit + 1):
        if d in primes:
            divisors.append(set([d]))
        else:
            divisors.append(set(primes.factorize(d).keys()))

        for n in range(ceil((d * best_num) / float(best_den)), (d * 3) // 7):
            if n * best_den > best_num * d and divisors[n].isdisjoint(divisors[d]):
                best_num = n
                best_den = d

    print(best_num)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
