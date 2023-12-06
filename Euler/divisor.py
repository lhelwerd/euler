"""
Module for calculating divisors of numbers.
"""

from typing import Set

def proper_divisors(number: int, add: int = 1) -> Set[int]:
    """
    Find proper divisors of `number`. `add` indicates the unitary value to add.
    """

    divisors = set()
    divisors.add(add)
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            divisors.add(divisor)
            divisors.add(number // divisor)

    return divisors
