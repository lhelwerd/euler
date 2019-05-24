# Sequences of numbers generated by a formula

import numpy as np
from past.builtins import xrange as range
from sortedcontainers import SortedSet

class FormulaSet(object):
    def __init__(self, formula, index, limit, extendable=True):
        self.formula = formula
        self.index = index
        self.numbers = SortedSet()
        self.start = 1
        self.limit = 1
        self.maximum = 0
        self.extendable = extendable
        self.extend(limit)

    def __iter__(self):
        return iter(self.numbers)

    def __len__(self):
        return len(self.numbers)

    def __reversed__(self):
        return reversed(self.numbers)

    def __getitem__(self, n):
        if not isinstance(n, slice) and n > self.limit:
            self.extend(n)

        return self.numbers[n]

    def extend(self, limit):
        if limit <= self.start:
            return

        self.start = self.limit
        self.limit = limit
        self.numbers.update(self.formula(np.array(range(self.start, self.limit + 1))))
        self.maximum = self.formula(self.limit)

    def __contains__(self, num):
        if self.extendable and num > self.maximum:
            # Determine which index we require. If the index function returns 
            # a float, then it doubles as a membership test in that the number
            # is part of the sequence if and only if the value is a natural
            # number. Otherwise the index must be at least or higher than
            # the index of the number in the sequence.
            index = self.index(num)
            if isinstance(index, float):
                return index == int(index)

            self.extend(index)

        return num in self.numbers
