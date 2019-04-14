"""
PROBLEM:     022
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Name scores from a list of names after alphabetically ordering them
    The name score of a name is defined as the position of the name in the
    ordered list (starting from 1) times the alphabetical value, calculated
    by the sum of the position in the alphabet of each character in the name.
"""

from bisect import bisect
import timeit
from Euler.text import read

def problem():
    names = read("p022_names.txt",
                 lambda result, word: result.insert(bisect(result, word), word))

    print(sum((i + 1) * sum(ord(c) - ord('A') + 1 for c in name)
              for (i, name) in enumerate(names)))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
