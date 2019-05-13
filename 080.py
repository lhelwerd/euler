"""
PROBLEM:     080
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of the first 100 digits in decimal expansions of the irrational square
    roots of the natural numbers up to 100.

    Use increased Decimal precision, more than 100 or 101 to calculate sqrt(5)
    correctly as its digits from 100 onward are 49695 thus continually rounding
    incorrectly at such precisions.
"""

import timeit
from decimal import Decimal, getcontext, Rounded

def problem():
    getcontext().prec = 128
    # Precalculate i = 2 and skip i = 100 (rational root)
    total = 475
    for i in range(3, 100):
        s = Decimal(i).sqrt()
        if getcontext().flags[Rounded]:
            total += sum(int(d) for d in str(s).replace('.', '')[:100])

        getcontext().clear_flags()

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
