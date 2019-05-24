"""
PROBLEM:     357
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of all integers n up to a hundred million for each divisor d of n,
    d + n / d is prime.
"""

import timeit
from Euler.formula import FormulaSet
from Euler.prime import PrimeSet

def problem():
    squares = FormulaSet(lambda n: n * n,
                         lambda num: math.sqrt(num),
                         10000)
    primes = PrimeSet(10**8 + 1)
    # 1 is also a valid answer
    total = 1
    for prime in primes:
        n = prime - 1
        if n not in squares:
            divs = primes.proper_divisors(n)
            for d in divs:
                if d * d <= n and d + n // d not in primes:
                    break
            else:
                total += n

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
