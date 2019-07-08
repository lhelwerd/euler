"""
PROBLEM:     105
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of optimum special sum sets A where |A| = n,
    the function S(V) := sum of x in V, S(A) is minimal,
    and for every two non-empty disjoint subsets B, C of A, (i) S(B) =/= S(C)
    and (ii) |B| > |C| ==> S(B) > S(C).
"""

import timeit
from Euler.special_subset_sum import special_subset_sum_set

def problem():
    total = 0
    with open('p105_sets.txt') as f:
        for line in f:
            values = tuple(int(d) for d in line.split(','))
            if special_subset_sum_set(values):
                total += sum(values)

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
