"""
PROBLEM:     048
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

from builtins import range
import timeit

def problem():
    print(str(sum(i ** i for i in range(1, 1000 + 1)))[-10:])

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
