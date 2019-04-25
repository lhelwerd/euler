"""
PROBLEM:     089
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Minimal form of Roman numeral
"""

import timeit
from Euler.roman import to_number, to_roman

def problem():
    original = 0
    new = 0
    with open('p089_roman.txt') as f:
        for line in f:
            numeral = line.rstrip()
            original += len(numeral)
            number = to_number(numeral)
            minimal = to_roman(number)
            new += len(minimal)

    print(original - new)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
