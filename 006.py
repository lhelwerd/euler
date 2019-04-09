"""
PROBLEM:     006
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Difference between squared sum and sum of sqares
"""

import timeit

def problem():
    n = 100
    n_sum = (n * (n + 1)) / 2.
    sq_sum = (n / 6.) * (2 * n + 1) * (n + 1)
    print(int((n_sum ** 2) - sq_sum))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

