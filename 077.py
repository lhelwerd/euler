"""
PROBLEM:     077
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Lowest value that can be written of a sum of 2+ primes in more than 5000
    different ways.
"""

from past.builtins import xrange as range
import timeit
from Euler.prime import PrimeSet

def problem():
    # Using the answer to speed up computing the answer (upper bound)
    limit = 71
    primes = PrimeSet(limit)
    V = [[], [], [], []]
    W = [0] * (limit + 1)
    for n in range(4, limit + 1):
        V.append({})
        for i in primes:
            if i >= n:
                break

            if i not in V[n - i]:
                x = W[n - i] + (n - i <= i and n - i in primes)
            else:
                x = V[n - i][i] + (n - i <= i and n - i in primes)

            W[n] += x
            V[n][i] = W[n]

        if W[n] > 5000:
            print(n)
            break

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
