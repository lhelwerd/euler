"""
PROBLEM:     051
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Smallest prime number where replacing some or all of the same digits in the
    number with the same digit (0 through 9 except for the first digit which
    cannot be 0), generates at least seven additional different primes.

Pseudocode:

- Generate some primes
- For each prime
  - For i = 1 .. num digits - 1
    - For each combination in itertools.combinations(range(num digits), i)
        - If digits at indexes are not the same (via set) then continue
        - If digit at indexes[0] is higher than 2 then continue
        - counter = 0
      - For j in range(max(digit[indexes[0]]), 1 if 0 in indexes else 0), 10)
        - Replace the digits at the given indexes with j
        - Check if the newly created number is prime -> count++
          - If count < 8 - (10 - j) then break (not enough primes in family)
      - If count == 8 then print the prime and exit
"""

from builtins import range
from itertools import combinations
import timeit
from Euler.prime import PrimeSet

def problem():
    primes = PrimeSet(10**6)
    find = 8
    for prime in primes:
        digits = str(prime)
        options = tuple(range(len(digits)))
        for i in range(1, len(digits)):
            for indexes in combinations(options, i):
                if int(digits[indexes[0]]) > 2:
                    continue
                if any(digits[k] != digits[indexes[0]] for k in indexes):
                    continue

                counter = 1
                for j in range(int(digits[indexes[0]]) + 1, 10):
                    new = ''.join(str(j) if i in indexes else digits[i] for i in options)
                    if int(new) in primes:
                        counter += 1
                    if counter < find - (10 - j):
                        break

                if counter >= find:
                    print(prime)
                    return


if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
