"""
PROBLEM:     021
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of all amicable numbers under 10000
    A number is amicable if the sum its proper divisors (so excluding itself)
    generates a pair number whose sum of proper divisors is the original number.
"""

from builtins import range
import timeit

def problem():
    amicable_sum = 0
    sums = {}

    n = 2
    while n < 10000:
        # Find divisors and add them up
        divisors = set()
        divisors.add(1)
        for i in range(2, n // 2):
            if n % i == 0:
                divisors.add(i)
                divisors.add(n // i)

        divisor_sum = sum(divisors)
        if divisor_sum in sums:
            if sums[divisor_sum] == n:
                amicable_sum += n + divisor_sum

            del sums[divisor_sum]
        else:
            sums[n] = divisor_sum

        n += 1

    print(amicable_sum)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

