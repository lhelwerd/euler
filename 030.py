"""
PROBLEM:     030
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of numbers that are the sum of fifth powers of their digits
"""

from builtins import range
import timeit

def problem():
    limit = 200000 # superset: http://oeis.org/A072896
    total = 0
    for n in range(10, limit):
        if n == sum(int(d) ** 5 for d in str(n)):
            total += n

    print(total)    

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
