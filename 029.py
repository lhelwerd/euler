"""
PROBLEM:     029
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Distinct terms of powers a^b with 2 <= a <= 100 and 2 <= b <= 100
"""

import timeit

def problem():
    terms = set()
    for a in range(2, 100 + 1):
        for b in range(2, 100 + 1):
            terms.add(a ** b)

    print(len(terms))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
