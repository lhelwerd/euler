from builtins import range
import math

def generate(limit):
    for part in range(1, limit / 10**(math.log10(limit) / 2)):
        digits = str(part)
        yield int(digits + digits[::-1])
        if len(digits) >= 2:
            yield int(digits + digits[len(digits) - 2::-1])
        else:
            yield part

def is_palindrome(digits):
    return digits == digits[::-1]
