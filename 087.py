"""
PROBLEM:     087
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of unique values that can be expressed as a sum of a prime square,
    prime cube and prime fourth power.
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    limit = 50 * 10**6
    limits = (int(limit ** .5), int(limit ** (1/3.)), int(limit ** .25))
    primes = PrimeSet(limits[0])
    values = set()
    for a in primes:
        for b in primes:
            if b > limits[1]:
                break
            for c in primes:
                if c > limits[2]:
                    break

                v = a ** 2 + b ** 3 + c ** 4
                if v < limit:
                    values.add(v)

    print(len(values))

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
