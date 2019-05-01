"""
PROBLEM:     076
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of ways that one hundred can be written as a sum of at least two
    positive integers.
"""

from past.builtins import xrange as range
import timeit

def problem():
    # NB To get the correct number for any i < d, adjust d to end at that
    # number instead
    d = 100
    W = [0] * (d+1)
    W[0] = 1
    # Inverted loop
    for i in range(1, d):
        for j in range(i, d + 1):
            # Count all previous options
            W[j] += W[j-i]

    print(W[d])

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
