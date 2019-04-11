from builtins import range

def path(filename):
    # Read a triangle file and find the maximum path sum in it.

    triangle = []
    M = []
    with open(filename) as numbers:
        for line in numbers:
            cols = line.strip().split(' ')
            triangle.append([int(c) for c in cols])
            M.append([0] * len(cols))

    M[0][0] = triangle[0][0]

    for row in range(1, len(triangle)):
        M[row] = [triangle[row][i] + max(M[row-1][i-1] if i > 0 else 0,
                                         M[row-1][i] if i < len(M[row-1]) else 0)
                  for i in range(len(triangle[row]))]

    return max(M[row])
