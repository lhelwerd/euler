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
        #print('changes direction')
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
        #print('better to get to {},{} from {},{}'.format(k, j, i, j))
        update(sums, matrix, back_edges, k, j, k + 1, j)
        # Update the back edges
        for p, q in back_edges.get((k, j), set()):
            #print('{},{} old: {}'.format(p, q, sums[p][q]))
            sums[p][q] = sums[k][j] + matrix[p][q]
            #print('new: {}'.format(sums[p][q]))

        #print(sums[k][j], sums[k+1][j])
        k -= 1

    # Update paths earlier in this row if our path is better
    l = j - 1
    while l >= 0 and sums[i][l] > sums[i][l+1] + matrix[i][l]:
        #print('better to get to {},{} from {},{}'.format(i, l, i, j))
        update(sums, matrix, back_edges, i, l, i, l + 1)
        # Update the back edges
        for p, q in back_edges.get((i, l), set()):
            #print('{},{} old: {}'.format(p, q, sums[p][q]))
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

    for m in range(1, n):
        #print(m)
        for p in range(0, m + 1):
            i = p
            j = m - p
            #print(i, j)
            calc(sums, matrix, back_edges, i, j)
    for m in range(n - 2, -1, -1):
        #print(n - 1 - m)
        for p in range(0, m + 1):
            i = n - 1 - p
            j = n - 1 - m + p
            #print(i, j)
            calc(sums, matrix, back_edges, i, j)
    #print([(k, b) for (k, b) in back_edges.iteritems() if len(b) > 1])

    #for i in range(n):
    #    print(sums[i])
    print(sums[n-1][n-1])

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
