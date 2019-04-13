"""
PROBLEM:     040
AUTHOR:      Leon Helwerda
STATUS:      {experimentation, in-progress, needs-optimization, done}
INTERPRETER: Python 2 or 3
EXPLANATION:
    Product of digits in Champernowne's constant
"""

import timeit

def problem():
    digits = 1
    product = 1
    i = 0
    limits = (10, 100, 1000, 10000, 100000, 1000000)
    pos = 10
    prev = 1
    while i < 6:
        while i < 6 and pos > limits[i]:
            n = 10 ** (digits - 1) + ((limits[i] - prev) / digits)
            digit = str(n)[(limits[i] - prev) % digits]
            product *= int(digit)
            i += 1
        digits += 1
        prev = pos
        pos += digits * (10 ** digits) - digits * (10 ** (digits - 1))

    print(product)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
