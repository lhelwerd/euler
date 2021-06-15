"""
PROBLEM:     159
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of the maximum digital root sums by factorizing each n between 2 and
    one million (excl.)
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    limit = 1000000
    primes = PrimeSet(limit)
    mdrs = [0] * limit
    total = 0
    for n in range(2, 10):
        mdrs[n] = n
        total += n
    for n in range(10, limit):
        s = n
        while s >= 10:
            s = sum(int(d) for d in str(s))

        if n in primes:
            mdrs[n] = s
            total += s
        else:
            best = s
            for i in range(9, 1, -1):
                if n % i == 0 and mdrs[n // i] + i > best:
                    best = mdrs[n // i] + i

            for factor in primes.proper_divisors(n):
                if mdrs[n // factor] + mdrs[factor] > best:
                    best = mdrs[n // factor] + mdrs[factor]

            mdrs[n] = best
            total += best

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
