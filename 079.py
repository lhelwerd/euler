"""
PROBLEM:     079
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    The shortest possible secret passcode of unknown length for which a keylog
    text file shows certain digits that were asked in order (but without the
    digit indexes).

    Assumes digits are unique in the passcode.
"""

import itertools
import timeit

def test_key(key, number):
    i = 0
    for d in key:
        j = number.find(d, i)
        if j == -1:
            return False
        i = j + 1 

    return True

def problem():
    digits = []
    with open('p079_keylog.txt') as f:
        for line in f:
            digits.append(line.rstrip())


    number = digits.pop()
    old = [number]
    d = 0
    c = 0
    while digits:
        if sum(digit in number for digit in digits[d]) >= 2:
            i = 0
            for digit in digits[d]:
                j = number.find(digit, i)
                if j == -1:
                    if digit in number[:i]:
                        new = number[:i].replace(digit, '', 1) + digit + number[i:]
                        if all(test_key(key, new) for key in old):
                            number = new
                        else:
                            c = d
                            d = d + 1 % len(digits)
                            break
                    else:
                        number = number[:i] + digit + number[i:]

                    i += 1
                else:
                    i = j + 1

            old.append(digits.pop(d))
            d = min(d, len(digits) - 1)
        else:
            c = d
            d = d + 1 % len(digits)

    print(number)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
