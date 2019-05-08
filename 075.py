"""
PROBLEM:     075
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of unique perimeters (sum of sides) value that have exactly one
    right angle triangles with {a,b,c} (so where a**2 + b**2 = c**2)
"""

from past.builtins import xrange as range
import math
import timeit
import numpy as np

def update(one, more, candidates):
    multi = candidates & one
    one -= multi
    more |= multi
    one |= candidates - more

matrices = [
    np.array([[1,-2,2],[2,-1,2],[2,-2,3]]),
    np.array([[1,2,2],[2,1,2],[2,2,3]]),
    np.array([[-1,2,2],[-2,1,2],[-2,2,3]])
]
limit = 1500000

def generate(triple, one, more):
    p = np.sum(triple)
    if p > limit:
        return

    candidates = set(p * np.arange(1, limit // p + 1))
    update(one, more, candidates)
    for matrix in matrices:
        generate(np.matmul(matrix, triple), one, more)

def problem():
    triple = np.array((3,4,5))
    one = set()
    more = set()
    generate(triple, one, more)
    print(len(one))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
