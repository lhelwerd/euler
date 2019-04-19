"""
PROBLEM:     060
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3
EXPLANATION:
    Lowest sum of a set of five primes for which any two primes concatenate
    to produce another prime.
"""

from past.builtins import xrange as range
from itertools import product
import timeit
from Euler.prime import PrimeSet

maximum = 5
def attempt(extend, start, total, best, primes):
    index = start
    first = True
    for add in primes[start:]:
        if first:
            index += 1
        extra = str(add)
        if all(primes.miller_test(int(exist + extra), 2) and primes.miller_test(int(extra + exist), 2) for exist in extend):
            first = False
            extend.add(extra)
            total += add
            if total > best:
                break
            if len(extend) >= maximum:
                return total, index

    return best, index

def problem():
    # Upper bound {13, 6733, 8389, 5197, 5701} found with 10**6 prime splitting
    best = 26072
    primes = PrimeSet(best)

    for j, option in enumerate(primes):
        total = option
        k = j
        while k < len(primes):
            best, k = attempt(set([str(option)]), k, total, best, primes)

    print(best)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
