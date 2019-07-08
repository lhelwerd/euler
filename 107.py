"""
PROBLEM:     107
AUTHOR:      Leon Helwerda
STATUS:      todo
INTERPRETER: Python 2 or 3
EXPLANATION:
    Maximum saving by removing edges with the most total weight while keeping
    the network connected, i.e., the minimum spanning tree.
"""

import timeit
import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree

def problem():
    edges = np.zeros((40, 40))
    with open('p107_network.txt') as f:
        for i, line in enumerate(f):
            for j, edge in enumerate(line.rstrip().split(',')):
                if edge != '-':
                    edges[i, j] = int(edge)

    mst = minimum_spanning_tree(edges)
    print(int(np.sum(np.triu(edges)) - np.sum(mst)))

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
