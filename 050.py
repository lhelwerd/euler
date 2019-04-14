"""
PROBLEM:     050
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Prime number below one million that can be expressed as the sum of the
    most consecutive primes
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(10**6 // 21)
    q = list(reversed(sorted(primes)))
    count = len(q)
    primes.extend(10**6)

    best_length = 21
    best_prime = 953
    for i in range(len(q) - 1):
        length = 1
        total = q[i] + q[i + 1]
        while total < 10**6 and i + length + 1 < count:
            length += 1
            if total in primes and length > best_length:
                best_length = length
                best_prime = total

            total += q[i + length]

    print(best_prime)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
