"""
PROBLEM:     055
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of potential Lychrel numbers, which after 50 iterations of adding
    the palindrome to the current iteration's number still does not yield a
    palindrome, below ten thousand
"""

from builtins import range
import timeit
from Euler.palindrome import is_palindrome

def problem():
    limit = 10000
    max_digits = 5
    max_iterations = 50
    iterations = [0] * limit
    value = list(range(limit))
    count = 0
    for i in range(limit - 1, 0, -1):
        digits = str(value[i])
        palindrome = False
        while not palindrome and iterations[i] < max_iterations:
            value[i] += int(digits[::-1])
            iterations[i] += 1
            digits = str(value[i])
            palindrome = is_palindrome(digits)

            # Skip through a known sequence
            if not palindrome and value[i] < limit:
                iterations[i] += iterations[value[i]]
                value[i] = value[value[i]]
                digits = str(value[i])
                palindrome = is_palindrome(digits)

        if not palindrome:
            count += 1

    print(count)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
