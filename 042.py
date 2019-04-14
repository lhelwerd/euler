"""
PROBLEM:     042
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Number of words that when summing their alphabetical values results in a
    triangle number which is in the sequence generated by t_n = 1/2 * n * (n+1).
"""

from builtins import range
import timeit
from Euler.text import read

triangle = set((n * (n + 1)) / 2 for n in range(1, 25))

def update_result(result, word):
    code = sum(ord(c) - ord('A') + 1 for c in word)
    if code in triangle:
        result.append(1)

def problem():
    t = read("p042_words.txt", update_result)
    print(len(t))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
