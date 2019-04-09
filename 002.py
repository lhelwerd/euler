"""
PROBLEM:     002
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of all even Fibonacci terms below four million.
"""

import timeit

def problem():
    first = 1
    second = 1
    even_sum = 0
    while second < 4e6:
        first, second = second, first + second
        if second % 2 == 0:
            even_sum += second

    print(even_sum)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
