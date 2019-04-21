"""
PROBLEM:     066
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    The number D for which the equation x^2 - Dy^2 = 1 has the highest minimal
    number x for which there is an integer solution for the equation.
"""

from decimal import Decimal
import math
import timeit
from Euler.continued_fraction import expand_sqrt

def problem():
    D = 1
    best_x = 0
    best_d = 0
    limit = 1000
    while D <= limit:
        if int(math.sqrt(D))**2 == D:
            D += 1
            continue

        # Pell's equation x^2 - Dy^2 = 1 has a minimal solution in x when going
        # through the sequence of convergent fractions of sqrt(D).
        s = Decimal(D).sqrt()
        period = [int((s + v) / w) for v, w in expand_sqrt(D)]
        i = 0
        x1 = 1
        x2 = int(s)
        y1 = 0
        y2 = 1 
        while i < len(period):
            x1, x2 = x2, x2 * period[i] + x1
            y1, y2 = y2, y2 * period[i] + y1
            i = (i + 1) % len(period)
            if x2 * x2 - D * y2 * y2 == 1:
                if x2 > best_x:
                    best_x = x2
                    best_d = D
                break

        D += 1

    print(best_d)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
