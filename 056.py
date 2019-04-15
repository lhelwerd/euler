"""
PROBLEM:     056
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Power number a^b with a, b < 100 which has the maximum sum of digits.
    Top-to-bottom, stop trying lower exponents if the number of digits * 9 is
    lower than the best found so far.
"""

from builtins import range
import timeit

def problem():
    limit = 100
    best = 0
    for a in range(limit - 1, 2, -1):
        b = limit - 1
        n = a ** b
        digits = str(n)
        while len(digits) * 9 > best:
            best = max(sum(int(d) for d in digits), best)
            n //= a
            digits = str(n)
            b -= 1

    print(best)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
