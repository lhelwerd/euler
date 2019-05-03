"""
PROBLEM:     085
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Area of grid that is closest to have two million different rectangles that
    fit within the grid.
"""

import timeit
import math
from decimal import Decimal

def problem():
    target = Decimal(2*10**6)
    height = lambda width: (Decimal(1) + (Decimal(16) * target) / (width**2 + width)).sqrt() / Decimal(2) - Decimal(1)
    count = lambda height, width: (int(height) * (int(height) + 1) / 2) * (int(width) * (int(width) + 1) / 2)
    
    w = 1
    h = 1
    area = 1
    best = target
    while w <= h:
        h = height(w)
        count1 = count(h, w)
        count2 = count(math.ceil(h), w)
        if best > abs(count1 - target):
            area = int(h) * w
            best = abs(count1 - target)
        if best > abs(count2 - target):
            area = int(math.ceil(h)) * w
            best = abs(count2 - target)

        w += 1

    print(area)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
