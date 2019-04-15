"""
PROBLEM:     053
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of selections C(n over r) with 1 <= n <= 100 which are greater than
    one million; using the Pascal triangle (dynamically programming each row
    based on the previous one).
"""

from builtins import range
import timeit

def problem():
    pascal = [0, 1]
    total = 0
    limit = 10 ** 6
    for n in range(1, 101):
        pascal = [
            pascal[r-1] + pascal[r] if r < len(pascal) else pascal[r-1]
            for r in range(1, n + 2)
        ]
        total += sum(c > limit for c in pascal)
        pascal[0:0] = [0]

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
