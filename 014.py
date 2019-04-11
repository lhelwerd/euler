"""
PROBLEM:     014
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Collatz' conjecture
"""

from builtins import range
import timeit

def problem():
    # Silly 0-indexers
    lengths = [0, 0]
    i = 2
    while i < 1e6:
        n = i
        steps = 0
        while n != 1 and n >= len(lengths):
            n = n / 2 if n % 2 == 0 else 3 * n + 1
            steps += 1

        lengths.append(steps + lengths[n])
        i += 1

    best = max(lengths)
    print("{} has the longest chain of {} steps".format(lengths.index(best), best))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

