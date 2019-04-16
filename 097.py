"""
PROBLEM:     097
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Last ten digits of the large non-Mersenne prime 28433 * 2^7830457 + 1.
"""

import timeit

def problem():
    print(str(28433 * pow(2, 7830457, 10**10) + 1)[-10:])

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
