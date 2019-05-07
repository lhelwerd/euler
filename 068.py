"""
PROBLEM:     068
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Maximum 16-digit string generated from a magic 5-gon ring

    Idea: 6 is the first digit in the string, as it is the lowest value of the
    five highest values, that are also on the outer nodes of the ring
    (otherwise the outer nodes would need to be larger on the other groups).
"""

from past.builtins import xrange as range
import timeit
from itertools import permutations

def problem():
    known = 6
    best = 0
    allowed = set((6, 7, 8, 9, 10))
    for placement in permutations(range(1, 6)):
        solution = [known] + [0] * 15
        total = known + placement[0] + placement[1]

        for i in range(1,6):
            solution[i*3-3] = total - placement[i-1] - placement[i%5]
            solution[i*3-2:i*3] = placement[i-1:i+1]
            if solution[i*3-3] not in allowed:
                break
        else:
            solution[-1] = placement[0]
            digits = int(''.join(str(d) for d in solution))
            best = max(best, digits)

    print(best)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
