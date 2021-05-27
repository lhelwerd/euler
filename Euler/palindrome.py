from builtins import range
import math

def generate(limit):
    """
    Generator providing palindromes. Palindromes are not provided in any
    specific order. Limit should be a power of ten.
    """

    length = int(math.log10(limit))

    for part in range(1, int(limit / 10**int(math.log10(limit) / 2))):
        digits = str(part)
        if len(digits) < length - 1:
            yield int(digits + digits[::-1])
        if len(digits) >= 2:
            yield int(digits + digits[len(digits) - 2::-1])
        else:
            yield part

def is_palindrome(digits):
    """
    Check if the provided string of digits is a palindrome.
    """

    return digits == digits[::-1]
