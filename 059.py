"""
PROBLEM:     059
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    XOR decryption using the knowledge that the text contains common English
    words.
"""

import string
import timeit

def problem():
    with open('/usr/share/dict/words') as dictionary:
        words = set(line.rstrip() for line in dictionary)

    longest = max(len(word) for word in words)

    with open('p059_cipher.txt') as cipher:
        numbers = tuple(int(c) for c in cipher.readline().rstrip().split(','))

    for a in range(97, 123):
        for b in range(97, 123):
            for c in range(97, 123):
                key = (a, b, c)
                text = ""
                total = 0
                common = 0
                for i, number in enumerate(numbers):
                    letter = chr(number ^ key[i % 3])
                    if letter == ' ':
                        if text.lower() not in words:
                            break

                        common += 1
                        text = ""
                    elif letter in string.ascii_letters:
                        text += letter

                    if len(text) > longest:
                        break

                    if common > 1:
                        break

                if text in words:
                    common += 1

                if common > 1:
                    print(sum(number ^ key[i % 3] for i, number in enumerate(numbers)))
                    return


if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
