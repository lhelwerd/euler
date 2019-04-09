"""
PROBLEM:     009
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Pythagorean triplet for which a + b + c = 1000
"""

from builtins import range
import timeit

def problem():
    # Euclid's formula, a variant
    for m in range(1, 1000, 2):
        for n in range(1, m, 2):
            a = m * n
            b = (m ** 2 - n ** 2) / 2
            c = (m ** 2 + n ** 2) / 2
            if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                print(a * b * c)
                return

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
