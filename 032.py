"""
PROBLEM:     032
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of all products c in expressions a * b = c whose terms are combined into
    a pandigital number.

    avoid symmetry by assuming a < b
    ensure a, b do not have 0 or duplicate digits
    ensure c, a, b do not have duplicate digits and 9 digits in total

    smallest value for a is 12 ~ 10
    smallest option is then c = b * 10
    so limit for a,b is b = c / 10 so one digit less than maximum of c
    maximum of c in these circumstances is 9876543 ~ 10 million
    so b is maximum of 1 million (divided by 10^(number of digits in a - 2)
"""

from builtins import range
import timeit

def problem():
    limit = 1000000
    products = set()
    digits = set("123456789")
    for a in range(2, limit):
        multiplicand = set(str(a))
        if '0' in multiplicand or len(multiplicand) < len(str(a)):
            continue

        for b in range(a + 1, limit / 10 ** len(multiplicand) - 2):
            multiplier = set(str(b))
            if '0' not in multiplier and multiplicand.isdisjoint(multiplier) and len(multiplier) == len(str(b)):
                prod = a * b
                if multiplicand | multiplier | set(str(prod)) == digits and len(str(prod)) == 9 - len(multiplier) - len(multiplicand):
                    products.add(prod)

    print(sum(products))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
