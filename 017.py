"""
PROBLEM:     017
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of letters in written-out numbers
"""

from builtins import range
import re
import timeit
from num2words import num2words as words

def problem():
    nonletters = re.compile(r'\W')
    print(sum(len(nonletters.sub('', words(i))) for i in range(1, 1000 + 1)))


if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

