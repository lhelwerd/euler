"""
PROBLEM:     196
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Sum of specific primes on two rows of a triangle, where those primes form
    a triple of primes with neighboring numbers in the triangle
"""

import timeit
from Euler.prime import PrimeSet

def check(primes, lengths, length, i, rows, row, end, backrow, backi):
    top = rows[0]
    cur = rows[row]
    if lengths[cur - top + i] == 0:
        return False
    if lengths[cur - top + i] >= length:
        return True

    if lengths[cur - top + i] < 0 and cur + i not in primes:
        lengths[cur - top + i] = 0
        return False

    l = length - 1
    if l == 0:
        lengths[cur - top + i] = max(lengths[cur - top + i], 1)
        return True

    lengths[cur - top + i] = 0
    total = 1
    # Don't check the direction we came from (43 -> 53 -> 43)
    # Left
    if (i > 0 and (row != backrow or i - 1 != backi) and \
        check(primes, lengths, l, i - 1, rows, row, end, row, i)):
        total += lengths[cur - top + i - 1]

    if total >= length:
        lengths[cur - top + i] = total
        return True

    # Right
    if (cur + i + 1 < end - 1 and cur + i + 1 < rows[row + 1] and \
        (row != backrow or i + 1 != backi) and \
         check(primes, lengths, l, i + 1, rows, row, end, row, i)):
        total += lengths[cur - top + i + 1]

    if total >= length:
        lengths[cur - top + i] = total
        return True

    # Above
    if row > 0:
        # Top-left
        if (i > 0 and \
            (row - 1 != backrow or i - 1 != backi) and \
            check(primes, lengths, l, i - 1, rows, row - 1, end, row, i)):
            total += lengths[rows[row - 1] - top + i - 1]

        if total >= length:
            lengths[cur - top + i] = total
            return True

        # Top
        if (i < rows[row] - rows[row - 1] and \
            (row - 1 != backrow or i != backi) and \
            check(primes, lengths, l, i, rows, row - 1, end, row, i)):
            total += lengths[rows[row - 1] - top + i]

        if total >= length:
            lengths[cur - top + i] = total
            return True

        # Top-right
        if (i < rows[row] - rows[row - 1] - 1 and \
            (row - 1 != backrow or i + 1 != backi) and \
            check(primes, lengths, l, i + 1, rows, row - 1, end, row, i)):
            total += lengths[rows[row - 1] - top + i + 1]

    if total >= length:
        lengths[cur - top + i] = total
        return True

    # Below
    if row < len(rows):
        # Bottom-left
        if (i > 0 and (row + 1 != backrow or i - 1 != backi) and \
            check(primes, lengths, l, i - 1, rows, row + 1, end, row, i)):
            total += lengths[rows[row + 1] - top + i - 1]

        if total >= length:
            lengths[cur - top + i] = total
            return True

        # Bottom
        if ((row + 1 != backrow or i != backi) and \
            check(primes, lengths, l, i, rows, row + 1, end, row, i)):
            total += lengths[rows[row + 1] - top + i]

        if total >= length:
            lengths[cur - top + i] = total
            return True

        # Bottom-right
        if ((row + 1 != backrow or i + 1 != backi) and \
            check(primes, lengths, l, i + 1, rows, row + 1, end, row, i)):
            total += lengths[rows[row + 1] - top + i + 1]

    lengths[cur - top + i] = total
    return True

def problem():
    primes = PrimeSet(20, extendable=False, miller=7)

    total = 0
    num = lambda row: (row * (row - 1)) // 2 + 1
    #S = (2, 3, 4, 5, 6)
    #S = (8, 9)
    #S = (10000,)
    S = (5678027, 7208785)

    # Track non-primes and if a prime triplet was found for a prime
    for row in S:
        rows = [
            num(row - 2), num(row - 1), num(row), num(row + 1), num(row + 2)
        ]
        end = num(row + 3)
        lengths = [-1] * (end - rows[0])

        for i in range(rows[3] - rows[2]):
            if check(primes, lengths, 3, i, rows, 2, end, -1, -1) and lengths[rows[2] - rows[0] + i] >= 3:
                total += rows[2] + i

        print(total)

    print(total)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
