"""
PROBLEM:     038
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Pandigital multiples
"""

from builtins import range
from itertools import permutations
import timeit

def problem():
    for i in permutations('987654321'):
        digits = ''.join(i)
        for j in range(1, 5):
            start = int(digits[:j])
            n = 2
            prod = str(start * n)
            k = len(prod) - 1
            while k < 9 and digits[k:].startswith(prod):
                k += len(prod)
                n += 1
                prod = str(start * n)

            if k == 9:
                print(digits)
                return

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
