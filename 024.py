"""
PROBLEM:     024
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    <explanation here>
"""

import math
import timeit

def alternative():
    import itertools
    p = int(1e6)
    print(''.join(str(j) for j in next(itertools.islice(itertools.permutations(range(0, 10)), p - 1, p))))

def problem():
    p = 1e6

    # Consider the order to be a recurrent formula with
    # s[1] = 1 and s[i] = s[i-1] * i for i > 1
    # Find the highest i for which s[i] < 1 million
    digits = []
    options = list(range(0, 10))
    while len(digits) < 10:
        s = 1
        i = 1
        while s < p:
            i += 1
            s = s * i

        # If we even did not start the recurrent formula then take the latest
        if i == 1:
            index = -1
        else:
            index = max(0, int(math.floor(p / (s / float(i)) - 0.0001)))

        digit = options[index]
        p = p % (s / i)
        options.remove(digit)
        digits.append(str(digit))

    print(''.join(digits))

if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
