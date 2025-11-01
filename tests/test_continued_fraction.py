"""
Unit tests for calculations involving continued fractions.
"""

import unittest
from decimal import Decimal

from Euler.continued_fraction import expand_sqrt


class ContinuedFractionTest(unittest.TestCase):
    """
    Tests for the continued fraction module.
    """

    def test_expand_sqrt(self) -> None:
        """
        Test the contiued fraction expansion of square root.
        """

        expansion = list(expand_sqrt(23))
        self.assertEqual(
            expansion,
            [
                (Decimal("4"), Decimal("7")),
                (Decimal("3"), Decimal("2")),
                (Decimal("3"), Decimal("7")),
                (Decimal("4"), Decimal("1")),
            ],
        )

        self.assertEqual(list(expand_sqrt(4)), [])
