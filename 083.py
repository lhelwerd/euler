"""
PROBLEM:     083
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Minimal path sum in a matrix of paths from top left to the bottom right
    that move left, right, down or up.
"""

from builtins import range
import timeit

def update(sums, matrix, back_edges, i, j, k, l):
    if (i,j) in back_edges and (k, l) in back_edges[(i, j)]:
        back_edges[(i,j)].discard((k, l))

    back_edges.setdefault((k,l), set())
    back_edges[(k,l)].add((i,j))
    sums[i][j] = sums[k][l] + matrix[i][j]

def calc(sums, matrix, back_edges, i, j):
    # Only take paths from above or left into account
    if i != 0 and (j == 0 or sums[i-1][j] < sums[i][j-1]):
        update(sums, matrix, back_edges, i, j, i - 1, j)
    else:
        update(sums, matrix, back_edges, i, j, i, j - 1)

    # Update paths higher in this column if our path is better
    k = i - 1
    while k >= 0 and sums[k][j] > sums[k+1][j] + matrix[k][j]:
        update(sums, matrix, back_edges, k, j, k + 1, j)
        # Update the back edges
        for p, q in back_edges.get((k, j), set()):
            sums[p][q] = sums[k][j] + matrix[p][q]

        k -= 1

    # Update paths earlier in this row if our path is better
    l = j - 1
    while l >= 0 and sums[i][l] > sums[i][l+1] + matrix[i][l]:
        # Update the back edges
        for p, q in back_edges.get((i, l), set()):
            sums[p][q] = sums[i][l] + matrix[p][q]
        
        l -= 1

def problem():
    matrix = []
    with open('p083_matrix.txt') as f:
        for line in f:
            matrix.append([int(c) for c in line.rstrip().split(',')])

    # Assume it's a square matrix
    n = len(matrix)
    sums = []
    for i in range(n):
        sums.append([0] * n)
    sums[0][0] = matrix[0][0]
    back_edges = {}

    # Top left part of matrix including antidiagonal
    for m in range(1, n):
        for p in range(0, m + 1):
            i = p
            j = m - p
            calc(sums, matrix, back_edges, i, j)

    # Bottom right part of matrix
    for m in range(n - 2, -1, -1):
        for p in range(0, m + 1):
            i = n - 1 - p
            j = n - 1 - m + p
            calc(sums, matrix, back_edges, i, j)

    print(sums[n-1][n-1])

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
