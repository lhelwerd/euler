"""
PROBLEM:     109
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of ways to finish a Darts round with a score less than 100 if the
    last dart must land on a double.
"""

from past.builtins import xrange as range
import timeit
from itertools import product, combinations_with_replacement

def problem():
    options = tuple(range(1, 21)) + (25,)
    multipliers = (1, 2, 3)
    p = set(product(options, multipliers))
    p.remove((25, 3))

    count = 0
    for score in range(2, 100):
        throws = set()
        for option in options:
            s = score - option * 2
            if s == 0:
                count += 1
            elif s > 0:
                for throw1 in p:
                    t = s - throw1[0] * throw1[1]
                    if t == 0:
                        throws.add((throw1, option))
                    elif t > 0:
                        for throw2 in p:
                            u = t - throw2[0] * throw2[1]
                            if u == 0:
                                throws.add((frozenset((throw1, throw2)), option))

        count += len(throws)

    print(count)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
