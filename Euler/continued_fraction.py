"""
Module for calculations involving continued fractions.
"""

from decimal import Decimal
from typing import Generator, Set, Tuple, Union

def expand_sqrt(number: int) -> Generator[Tuple[Decimal, Decimal], None, None]:
    """
    Generate the unique parameters of the continued fraction expansion of
    the square root of `number`, stopping when an existing parameter is found.
    """

    square_root = Decimal(number).sqrt()
    if square_root % 1 != 0:
        fraction: Union[int, Decimal] = int(square_root)
        expansions: Set[Tuple[Decimal, Decimal]] = set()
        # Numerator/denominator start values like sqrt(2) expansion
        numerator = Decimal('0')
        denominator = Decimal('1')
        while (numerator, denominator) not in expansions:
            # Not yet found, so add to the known expansions
            expansions.add((numerator, denominator))
            if numerator != 0:
                yield (numerator, denominator)

            # Calculate next expansion's paramters
            # First iteration: v0 = int(s), w0 = n - int(s)**2 (n = s**2)
            #  --> e.g. for s = sqrt(23) we get v0 = 4, w0 = 23 - 16 = 7
            # v_i = int((v_{i-1} + s) /  w_{i-1}) * w_{i-1} - v{i-1},
            # w_i = int((n - v_i ** 2) / w_{i-1})
            #  --> e.g. for s = sqrt(23) we get
            #  v1 = int((4+4...)/7) * 7 - 4 = 3, w1 = (23 - 3**2) / 7 = 2
            numerator = fraction * denominator - numerator
            denominator = (number - numerator ** 2) // denominator
            fraction = (numerator + square_root) // denominator
