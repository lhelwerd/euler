"""
PROBLEM:     206
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    A square of the form 1_2_3_4_5_6_7_8_9_0 where each _ is a single digit.
"""

import timeit
import math

def problem():
    start = int(math.sqrt(1020304050607080900))
    limit = int(math.sqrt(1929394959697989990))
    d = start
    while d < limit:
        digits = str(d * d)
        if digits[::2] == '1234567890':
            print(d)
            return
        elif digits[::2] > '1234567890':
            # Try to skip over impossible root
            v = int(2 * (math.log10(int(digits[::2]) - 1234567890) + 1) + 1) // 2 * 2
            old = d
            if digits[-v] == '9':
                # Gotta go over this one
                d = int(math.sqrt(d * d - 10 ** (v - 1) + 10 ** (v - 2)))
                v += 2

            d = int(math.sqrt(d * d + 10 ** (v - 1) - 10 ** (v - 2)))
            if old >= d:
                # Unfortunately this attempt may fail and we could end up on 
                # the same root which would halt our process, so fall back on 
                # just +1
                d = old + 1
        else:
            d += 1

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
