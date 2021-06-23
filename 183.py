"""
PROBLEM:     183
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of N or -N with 5<=N<=10000 where we select N if the maximization of
    (N/k)**k is a non-terminating decimal and -N otherwise.
"""

import math
import timeit

def check_factors(n, d):
    """
    Check if n/d is a terminating decimal in base 10, i.e. the denominator
    has at most factors 2 and 5 after simplication (but with an optimization
    we can perform simplication after factorization and not care about GCD)
    """

    while d % 2 == 0:
        d //= 2
    while d % 5 == 0:
        d //= 5

    if n % d == 0:
        # Simplification
        return True

    return d == 1

def problem():
    start = 5
    limit = 10000
    total = 0
    k_exp = [0, 0]
    # Curious situation: n / best_k approaches e
    k_exp.extend(k ** k for k in range(2, math.ceil(limit / math.e) + 1))
    best_k = 2
    for n in range(start, limit + 1):
        best_num = 0
        best_den = 1
        for k in range(best_k, best_k + 2): # previous best or +1
            num = n ** k
            den = k_exp[k]
            if num * best_den > best_num * den:
                best_num = num
                best_den = den
                best_k = k

        if check_factors(best_num, best_den):
            # Terminating decimal representation
            total -= n
        else:
            total += n

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
