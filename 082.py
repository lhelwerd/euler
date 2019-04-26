"""
PROBLEM:     082
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Minimal path sum in a matrix of paths between the leftmost and rightmost
    columns that move right, down or up.
"""

from builtins import range
import timeit

def problem():
    matrix = []
    with open('p082_matrix.txt') as f:
        for line in f:
            matrix.append([int(c) for c in line.rstrip().split(',')])

    # Assume it's a square matrix
    n = len(matrix)
    sums = []
    for i in range(n):
        sums.append([0] * n)
        sums[i][0] = matrix[i][0]

    for j in range(1, n):
        sums[0][j] = sums[0][j-1] + matrix[0][j]
        for i in range(1, n):
            # Only take paths from above or left into account
            sums[i][j] = min(sums[i-1][j], sums[i][j-1]) + matrix[i][j]

            # Update paths higher in this column if our path is better
            k = i - 1
            while k >= 0 and sums[k][j] > sums[k+1][j] + matrix[k][j]:
                sums[k][j] = sums[k+1][j] + matrix[k][j]
                k -= 1

    print(min(sums[i][n-1] for i in range(n)))

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

