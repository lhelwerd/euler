"""
PROBLEM:     106
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of same-sized pairs of subsets of a set with n = 12 elements for
    which the first rule for special sum sets A where |A| = n,
    the function S(V) := sum of x in V, S(A) is minimal, needs to be tested.

    http://oeis.org/A304011
"""

import timeit
from scipy.special import binom

def problem():
    total = 0
    n = 12
    for i in range(1, n // 2 + 1):
        total += binom(n, 2 * i) * binom(2 * i - 1, i - 2)

    print(int(total))

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
