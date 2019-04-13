"""
PROBLEM:     004
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Largest palindrome of the product of two 3-digit numbers
"""

import timeit
from Euler.palindrome import is_palindrome

def problem():
    largest = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            prod = i * j
            if is_palindrome(str(prod)) and prod > largest:
                largest = prod

    print(largest)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
