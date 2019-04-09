"""
PROBLEM:     004
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3
EXPLANATION:
    Largest palindrome of the product of two 3-digit numbers
"""

import timeit

def problem():
    largest = 0
    for i in range(1000, 99, -1):
        for j in range(1000, 99, -1):
            if str(i * j) == ''.join(list(reversed(str(i * j)))):
                if largest < i * j:
                    largest = i * j

    print(largest)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
