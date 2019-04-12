"""
PROBLEM:     026
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Repeating decimals in fractions
"""

from builtins import range
import timeit

def problem():
    lengths = [0]*1000
    for i in range(2, 1000):
        if i % 2 == 0 or i % 5 == 0:
            # Terminating so at most 1 (I think?)
            lengths[i] = 1
        else:
            p = 2
            while (10 ** p) % i != 1:
                p += 1
            lengths[i] = p

    print(lengths.index(max(lengths)))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

