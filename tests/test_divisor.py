"""
Unit tests for calculations divisors of numbers.
"""

import unittest
from Euler.divisor import proper_divisors

class DivisorTest(unittest.TestCase):
    """
    Tests for the divisor module.
    """

    def test_proper_divisors(self) -> None:
        """
        Test the proper divisor search.
        """

        self.assertEqual(proper_divisors(10), {1, 2, 5})
