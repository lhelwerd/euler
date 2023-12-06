"""
Unit tests for converting Roman numerals.
"""

import unittest
from Euler.roman import to_number, to_roman

class RomanTest(unittest.TestCase):
    """
    Tests for the roman module.
    """

    def test_to_number(self) -> None:
        """
        Test the conversion from Roman numeral to number.
        """

        self.assertEqual(to_number('XVI'), 16)
        self.assertEqual(to_number('MCMXCIX'), 1999)

    def test_to_roman(self) -> None:
        """
        Test the conversion from number to Roman numeral.
        """

        self.assertEqual(to_roman(52), 'LII')
        self.assertEqual(to_roman(2019), 'MMXIX')
