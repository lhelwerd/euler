"""
PROBLEM:     086
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Spider and fly problem
"""

import timeit
import numpy as np

matrices = [
    np.array([[1,-2,2],[2,-1,2],[2,-2,3]]),
    np.array([[1,2,2],[2,1,2],[2,2,3]]),
    np.array([[-1,2,2],[-2,1,2],[-2,2,3]])
]

def problem():
    target = 10**6
    M = 0
    sol = 0
    triples = [(np.array((3,4,5)), 1)]
    expand = [np.array((3,4,5))]
    seen = set([(3, 4, 5)])
    while sol < target:
        M += 1
        i = 0
        while i < len(triples):
            triple, mult = triples[i]
            ok = (triple[0] * mult <= 2 * M and triple[1] * mult <= M,
                  triple[1] * mult <= 2 * M and triple[0] * mult <= M)
            if True in ok:
                found = False
                for j, k in enumerate(ok):
                    if k and triple[abs(j-1)] * mult == M:
                        # How many possible solutions are encoded in triple[j],
                        # (w + h), excluding rotations (so a <= b)?
                        if triple[j] * mult < M:
                            sol += triple[j] * mult // 2
                        else:
                            sol += 1 + M - (triple[j] * mult + 1) // 2
                        found = True

                if found:
                    i += 1
                elif triple[0] * mult < M and triple[1] * mult < M:
                    del triples[i]
                    seen.remove(tuple(triple * mult))
                else:
                    i += 1

                # Limit growth of non-primitive pythagorean triples
                if triple[0] * mult == M or triple[1] * mult == M:
                    # Ensure we haven't seen this triple already
                    s = tuple(triple * (mult + 1))
                    if s not in seen:
                        triples.append((triple, mult + 1))
                        seen.add(s)
            else:
                i += 1

        # Expand primitive pythagorean triples
        primitives = []
        for primitive in expand:
            # Limit growth of primitives
            if min(primitive[0], primitive[1]) == M:
                for matrix in matrices:
                    expanded = np.matmul(matrix, primitive)
                    triples.append((expanded, 1))
                    primitives.append(expanded)
                    seen.add(tuple(expanded))
            else:
                primitives.append(primitive)
        expand = primitives

    print(M)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
