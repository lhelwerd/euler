"""
PROBLEM:     098
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Largest square number formed by a word or one of its anagrams by replacing
    the word with an injective mapping of digits (avoiding leading zeros).
"""

import itertools
import math
import timeit
from Euler.formula import FormulaSet
from Euler.text import read

def problem():
    words = read('p098_words.txt')
    limit = 10**6
    squares = FormulaSet(lambda n: n * n,
                         lambda num: math.sqrt(num),
                         limit)

    maximum_square = 1
    seen = set()
    for word in words:
        if word in seen or len(word) < math.log10(maximum_square):
            continue

        sorted_word = sorted(word)
        anagrams = set(anagram for anagram in words if sorted(anagram) == sorted_word and anagram != word)
        if not anagrams:
            continue

        seen.update(anagrams)

        letters = dict((p[1], p[0]) for p in enumerate(sorted(set(word))))
        first_letter = letters[word[0]]
        for replacement in itertools.permutations(range(10), len(letters)):
            if replacement[first_letter] == 0:
                continue

            number = int(''.join(str(replacement[letters[letter]]) for letter in word))
            if number in squares:
                for anagram in anagrams:
                    if replacement[letters[anagram[0]]] == 0:
                        continue

                    number2 = int(''.join(str(replacement[letters[letter]]) for letter in anagram))
                    if number2 in squares:
                        maximum_square = max(maximum_square, max(number, number2))

    print(maximum_square)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
