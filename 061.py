"""
PROBLEM:     061
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of the six 4-digit numbers for which each subsequent number's first two
    digits are the same as the last two digits of the previous number in their
    arrangement, also cyclically, and there is a triangular number, square
    number, pentagonal number, hexagonal number, heptagonal number and
    octagonal number - each representated by a different number in the set.

    Triangular: P3,n = n(n+1)/2
    Square:     P4,n = n^2
    Pentagonal: P5,n = n(3n-1)/2
    Hexagonal:  P6,n = n(2n-1)
    Heptagonal: P7,n = n(5n-3)/2
    Octagonal:  P8,n = n(3n-2)
"""

from past.builtins import xrange as range
from copy import copy
import math
import timeit
from Euler.formula import FormulaSet

class Problem(object):
    def __init__(self):
        self.partial_start = 10
        self.partial_limit = 99
        self.start = self.partial_start * 100 + self.partial_start
        self.limit = self.partial_limit * 100 + self.partial_limit
        self.count = 6

        self.formulae = (
            # Triangular
            FormulaSet(lambda n: n * (n + 1) / 2.,
                       lambda num: ((math.sqrt(8 * num + 1) - 1) / 2),
                       self.limit),
            # Square
            FormulaSet(lambda n: n * n,
                       lambda num: math.sqrt(num),
                       self.limit),
            # Pentagonal
            FormulaSet(lambda n: n * (3 * n - 1) / 2.,
                       lambda num: ((math.sqrt(24 * num + 1) + 1) / 6),
                       self.limit),
            # Hexagonal
            FormulaSet(lambda n: n * (2 * n - 1),
                       lambda num: ((math.sqrt(8 * num + 1) + 1) / 4),
                       self.limit),
            # Heptagonal
            FormulaSet(lambda n: n * (5 * n - 3) / 2.,
                       lambda num: ((math.sqrt(40 * num + 9) + 3) / 10),
                       self.limit),
            # Octagonal
            FormulaSet(lambda n: n * (3 * n - 2),
                       lambda num: ((math.sqrt(3 * num + 1) + 1) / 3),
                       self.limit)
        )

    def represent(self, matches, x=None):
        if x is None:
            x = set(range(self.count))
        elif not x:
            return True

        for option in matches[0]:
            if option in x and self.represent(matches[1:], x - set([option])):
                return True

        return False

    def attempt(self, i, numbers, x, matches, start):
        match = frozenset(i for i, f in enumerate(self.formulae) if x in f)
        if len(match) == 0 or any(match.issubset(m) for m in matches):
            return False, numbers, matches

        numbers.append(x)
        matches.append(match)
        if i == 6:
            ok = x % 100 == start // 100 and self.represent(matches)
            return ok, numbers, matches

        i += 1
        digits = (x % 100) * 100
        y = self.partial_start
        while y <= self.partial_limit:
            number = digits + y
            if number not in numbers:
                ok, n, m = self.attempt(i, copy(numbers), number, copy(matches), start)
                if ok:
                    return ok, n, m

            y += 1

        return False, numbers, matches

    def execute(self):
        for x in range(self.start, self.limit + 1):
            ok, numbers, matches = self.attempt(1, [], x, [], x)

            if ok:
                return sum(numbers)

def problem():
    p = Problem()
    print(p.execute())

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
