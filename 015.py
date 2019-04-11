"""
PROBLEM:     015
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of lattice paths
"""

import math
import timeit

def problem():
    # Number of lattice paths from (0,0) to (n,k) is equal to the binomial
    # coefficient n + k over n or (n + k)! / (n! * k!).
    n = 20
    k = 20
    print(math.factorial(n + k) // (math.factorial(n) * math.factorial(k)))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

