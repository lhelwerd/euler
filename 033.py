"""
PROBLEM:     033
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Lowest common denominator of the product of all non-trivial digit-cancelling
    fractions with two digits in nominator and denominator, where one common
    digit (not a zero) in both parts can be removed to obtain a fraction with
    the same value which is less than one.
"""

from builtins import range
from fractions import Fraction
import timeit

def problem():
    fractions = set()
    for n in range(10, 100):
        nom = str(n)
        for d in range(n + 1, 100):
            den = str(d)
            for common in (set(nom) & set(den)) - set('0'):
                n2 = int(nom[nom.find(common) - 1])
                d2 = int(den[den.find(common) - 1])
                if n2 != 0 and d2 != 0 and Fraction(n, d) == Fraction(n2, d2):
                    fractions.add((n, d))

    total = Fraction(1, 1)
    for fraction in fractions:
        total *= Fraction(*fraction)
    print(total.denominator)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
