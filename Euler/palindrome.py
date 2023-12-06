"""
Module for palindromes.
"""

import math
from typing import Generator

def generate(limit: int) -> Generator[int, None, None]:
    """
    Generator providing palindromes. Palindromes are not provided in any
    specific order. `limit` should be a power of ten.
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

def is_palindrome(digits: str) -> bool:
    """
    Check if the provided string `digits` is a palindrome.
    """

    return digits == digits[::-1]
