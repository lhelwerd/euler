"""
PROBLEM:     243
AUTHOR:      Leon Helwerda
STATUS:      needs-optimization
INTERPRETER: Python 2 or 3 (PyPy)
EXPLANATION:
    Smallest denominator which has a ratio of proper fractions which can be
    cancelled down to a simpler fraction less than 15499/94744.

    - Use Euler's totient function
    - Skip primes - none of the fractions can be cancelled so phi(p) = 1 and
      R(p) = 1 - but only check if number is a prime after trying some divisors
"""

import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(10**6, extendable=False, miller=4)
    d = 1
    phi = 1
    phis = [0, 1]
    target_numerator = 15499
    target_denominator = 94744
    check = 10**6
    while phi * target_denominator >= target_numerator * (d - 1):
        d += 1
        phi = primes.totient(d, phis)

    print(d)

if __name__ == "__main__":
    problem()
