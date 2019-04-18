"""
PROBLEM:     092
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Amount of numbers that end up at 89 if the sum of their digits are squared
    until their get stuck in a loop (which happens at either 89 or 1).
"""

import timeit

def digit_square(number):
    while number != 0:
        yield (number % 10) ** 2
        number //= 10

def problem():
    to_one = set([1])
    to_eightynine = set([89])
    count = 0
    limit = 10**7
    for i in range(limit - 1, 0, -1):
        number = i
        seen = set()
        while number not in to_one and number not in to_eightynine:
            seen.add(number)
            number = sum(digit_square(number))

        if number in to_one:
            to_one.update(seen)
        else:
            to_eightynine.update(seen)

    print(len(to_eightynine))

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
