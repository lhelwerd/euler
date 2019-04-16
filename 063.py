"""
PROBLEM:     063
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of n-digit numbers which can be expressed as an nth power.
"""

import timeit

def problem():
    n = 1
    count = 1
    total = 0
    minimum = 1
    while count > 0:
        count = 0
        i = minimum
        length = 1
        while length < n + 1:
            length = len(str(i ** n))
            i += 1
            if length < n:
                minimum += 1
            elif length == n:
                count += 1

        total += count
        n += 1

    print(total)
        

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
