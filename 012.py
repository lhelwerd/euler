"""
PROBLEM:     012
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    First triangle number with over five hundred divisors
"""

import timeit

def problem():
    triangle = 0
    i = 1
    divisors = 0
    while divisors < 500:
        triangle += i
        divisors = 1
        n = triangle
        j = 2
        factor = 0

        # Perform a prime factorization and calculate the number of divisors 
        # according to https://math.stackexchange.com/a/1853205:
        # if n = p1^e1 * p2^e2 * ... * pr^er then the number of divisors is
        # (e1 + 1) * (e2 + 1) * ... * (er + 1).
        while j * j <= n:
            if n % j == 0:
                factor += 1
                n //= j
            else:
                if factor != 0:
                    divisors *= factor + 1
                    factor = 0
                j += 1

        divisors *= factor + 1
        if n > 1 and n % j != 0:
            divisors *= 2

        i += 1

    print("{} has {} divisors".format(triangle, divisors))


if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
