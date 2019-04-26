"""
PROBLEM:     081
AUTHOR:      Leon Helwerda
STATUS:      {experimentation, in-progress, needs-optimization, done}
INTERPRETER: Python 2 or 3
EXPLANATION:
    Minimal path sum in a matrix of paths that only move right or down between
    the cells of the matrix.
"""

from builtins import range
import timeit

def problem():
    matrix = []
    with open('p081_matrix.txt') as f:
        for line in f:
            matrix.append([int(c) for c in line.rstrip().split(',')])

    # Assume it's a square matrix
    n = len(matrix)
    sums = []
    for i in range(n):
        sums.append([0] * n)

    sums[0][0] = matrix[0][0]
    for i in range(1, n):
        sums[i][0] = sums[i-1][0] + matrix[i][0]
    for j in range(1, n):
        sums[0][j] = sums[0][j-1] + matrix[0][j]

    for i in range(1, n):
        for j in range(1, n):
            sums[i][j] = min(sums[i-1][j], sums[i][j-1]) + matrix[i][j]

    print(sums[n-1][n-1])

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
