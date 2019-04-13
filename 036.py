"""
PROBLEM:     036
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of all numbers less than one million which are palindromes in base 10
    and in base 2.
"""

from builtins import range
import math
import timeit
from Euler.palindrome import generate, is_palindrome

def problem():
    limit = int(1e6)
    total = 0
    for i in generate(limit):
        if is_palindrome(bin(i)[2:]):
            total += i

    print(total)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
