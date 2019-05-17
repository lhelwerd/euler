"""
PROBLEM:     078
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Lowest value that for which the number of partitions into sums (plus one)
    is divisible by one million.
"""

from past.builtins import xrange as range
import timeit
import numpy as np

def problem():
    target = 10**6
    Partitions = [1]
    n = 0
    p = 1
    while p % target != 0:
        n += 1
        k = 1
        p = 0
        i = n - 1
        while i >= 0:
            if k % 2 != 0:
                p += Partitions[i]
            else:
                p -= Partitions[i]

            if k < 0:
                k = k * -1 + 1
            else:
                k = k * -1

            i = n - k * (3 * k - 1) / 2

        Partitions.append(p)

    print(n)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
