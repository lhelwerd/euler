"""
PROBLEM:     111
AUTHOR:      Leon Helwerda
STATUS:      {experimentation, in-progress, needs-optimization, done}
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of 10-digit prime numbers where a digit is repeated maximally
"""

import itertools
import numpy as np
import timeit
from past.builtins import xrange as range
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(10**6, miller=5)
    n = 10
    total = 0
    for d in range(0, 10):
        for M in range(n - 1, 0, -1):
            S = 0
            start = 1 if d == 0 else 0

            for pos in itertools.combinations(range(start, n), M):
                same = np.zeros(n, dtype=bool)
                same[(pos,)] = 1
                diff = ~same
                digits = np.empty(n, dtype=int)

                begin = 0 if pos[0] == 0 else 1
                first = list(range(begin, d)) + list(range(d + 1, 10))
                others = list(range(0, d)) + list(range(d + 1, 10))
                product = [first] + [others] * (n - M - 1)
                for rep in itertools.product(*product):
                    digits[same] = d
                    digits[diff] = rep
                    num = int(''.join(str(d) for d in digits))
                    if num in primes:
                        S += num

            if S > 0:
                total += S
                break

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
