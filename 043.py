"""
PROBLEM:     043
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of all pandigital digits with digits from 0 through 9 whose 3-digit
    substrings except the starting substring are divisible by the increasing
    prime numbers while progressing through the number by one digit each.
"""

from itertools import permutations
import timeit

def problem():
    primes = (2, 3, 5, 7, 11, 13, 17)
    total = 0
    for digits in permutations('0123456789'):
        if digits[0] != '0':
            i = 2 # 0-indexing ahead
            sub = int(''.join(digits[i-1:i+2]))
            while i <= 8 and sub % primes[i-2] == 0:
                i += 1
                sub = int(''.join(digits[i-1:i+2]))

            if i > 8:
                total += int(''.join(digits))

    print(total)

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
