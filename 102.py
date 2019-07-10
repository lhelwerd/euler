"""
PROBLEM:     102
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of triangles that contain the origin
"""

import timeit

def problem():
    sign = lambda x1, y1, x2, y2: -x2 * (y1 - y2) + y2 * (x1 - x2)
    count = 0
    with open('p102_triangles.txt') as f:
        for line in f:
            p = tuple(int(d) for d in line.rstrip().split(','))
            # Test if origin is within the triangle by checking each side and 
            # only counting if the directions are not different
            s1 = sign(p[0], p[1], p[2], p[3])
            s2 = sign(p[2], p[3], p[4], p[5])
            s3 = sign(p[4], p[5], p[0], p[1])
            neg = s1 < 0 or s2 < 0 or s3 < 0
            pos = s1 > 0 or s2 > 0 or s3 > 0
            count += not (neg and pos)

    print(count)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
