"""
PROBLEM:     020
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of digits in factorial of 100
"""

import math
import timeit

def problem():
    # 100! has the same digits as 99! except two extra zeroes at the end
    print(sum(int(d) for d in str(math.factorial(99))))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
