"""
PROBLEM:     125
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of palindromes below 10**8 that can be written as the sum of consecutive
    squares of positive integers
"""

import timeit
from Euler.palindrome import is_palindrome

def problem():
    palindromes = set()
    limit = int(10**8)

    squares = [x ** 2 for x in range(1, int(limit ** 0.5))]
    for i in range(len(squares) - 1):
        pali = squares[i]
        for j in range(i + 1, len(squares)):
            pali += squares[j]
            if pali >= limit:
                break
            if is_palindrome(str(pali)):
                palindromes.add(pali)

    print(sum(palindromes))

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
