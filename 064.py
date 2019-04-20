"""
PROBLEM:     064
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of continued fractions of n <= 10000 that have an odd period when
    expanding the fraction.
"""

from past.builtins import xrange as range
from decimal import Decimal
import timeit

def problem():
    odd = 0
    limit = 10000
    for n in range(1, limit + 1):
        s = Decimal(n).sqrt()
        if s % 1 != 0:
            x = s
            f = int(s)
            P = set()
            # Numerator/denominator start values like sqrt(2) expansion #57
            v = Decimal('0')
            w = Decimal('1')
            while (v, w) not in P:
                # Not yet found, so add to the known expansions
                P.add((v, w))
                # Calculate next expansion
                # First iteration: v0 = int(s), w0 = n - int(s)**2 (n = s**2)
                #  --> e.g. for s = sqrt(23) we get v0 = 4, w0 = 23 - 16 = 7
                # v_i = int((v_{i-1} + s) / w_{i-1}) * w_{i-1} - v{i-1},
                # w_i = int((n - v_i ** 2) / w_{i-1})
                #  --> e.g. for s = sqrt(23) we get
                #  v1 = int((4+4...)/7) * 7 - 4 = 1, w1 = (23 - 1**2) / 7 = 3
                v = f * w - v
                w = (n - v ** 2) // w
                x = (v + s) // w
                f = int(x)

            # One extra
            if len(P) % 2 == 0:
                odd += 1

    print(odd)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
