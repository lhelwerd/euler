"""
PROBLEM:     099
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Line number of a base/exponent pair that is the largest of all pairs in
    a file.

    a^b >? c^d
    powers are too large to construct

    raise to 1/(bd) power

    a^b^[1/(bd)] >? c^d^[1/(bd)]
    a^[b/bd] >? c^[d/bd]
    a^[1/d] >? c^[1/b]

    Use Decimal to increase the precision that is used by default.
    From https://docs.python.org/3/library/decimal.html#decimal.Context.power:
    ```
    The C module computes `power()` in terms of the correctly-rounded `exp()`
    and `ln()` functions. The result is well-defined but only ``almost always
    correctly-rounded''.
    ```
"""

import timeit
from decimal import Decimal

def problem():
    best_line = 0
    best_base = Decimal(0)
    best_exp = Decimal(1)
    with open('p099_base_exp.txt') as f:
        for i, line in enumerate(f):
            numbers = line.rstrip().split(',')
            base = Decimal(numbers[0])
            exp = Decimal(numbers[1])
            if base ** (1 / best_exp) > best_base ** (1 / exp):
                best_line = i
                best_base = base
                best_exp = exp

    # Adjust for zero-indexing
    print(best_line + 1)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
