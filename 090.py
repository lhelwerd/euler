"""
PROBLEM:     090
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of dice arrangements with which all nine square numbers below 100
    can be displayed.
"""

from itertools import combinations
import timeit

squares = [
    (lambda d: 0 in d, lambda d: 1 in d),
    (lambda d: 0 in d, lambda d: 4 in d),
    (lambda d: 0 in d, lambda d: 6 in d or 9 in d),
    (lambda d: 1 in d, lambda d: 6 in d or 9 in d),
    (lambda d: 2 in d, lambda d: 5 in d),
    (lambda d: 3 in d, lambda d: 6 in d or 9 in d),
    (lambda d: 4 in d, lambda d: 6 in d or 9 in d),
    (lambda d: 6 in d or 9 in d, lambda d: 4 in d),
    (lambda d: 8 in d, lambda d: 1 in d)
]

def problem():
    count = 0
    for d1 in combinations(range(10), 6):
        if all(one(d1) or two(d1) for one, two in squares):
            for d2 in combinations(range(10), 6):
                for one, two in squares:
                    if not ((one(d1) and two(d2)) or (one(d2) and two(d1))):
                        break
                else:
                    count += 1

    print(count / 2)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
