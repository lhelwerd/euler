"""
PROBLEM:     093
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Set of four numbers with which the longest range of consecutive numbers
    starting from 1 can be generated through expressions using +, -, *, and /
    (and parentheses).
"""

from __future__ import division
import itertools
import operator
import timeit

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def get_operations(x, y):
    for name, op in operations.items():
        try:
            yield op(x, y)
        except ZeroDivisionError:
            pass

def get_expressions(digits, subtotal=None):
    if not digits:
        return set((subtotal,))

    extra = set()
    if subtotal is None:
       for pair in itertools.permutations(digits, 2):
            for op in get_operations(*pair):
                extra.update(get_expressions(digits - set(pair), op))
    else:
        for x in digits:
            remain = digits - set((x,))
            for op in get_operations(x, subtotal):
                extra.update(get_expressions(remain, op))
            for op in get_operations(subtotal, x):
                extra.update(get_expressions(remain, op))

    return extra

def problem():
    n = 1
    abcd = ""
    for digits in itertools.combinations(range(1, 10), 4):
        result = get_expressions(frozenset(digits))
        i = 1
        while i in result:
            i += 1

        if i > n:
            n = i
            abcd = ''.join(str(d) for d in digits)

    print(abcd)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
