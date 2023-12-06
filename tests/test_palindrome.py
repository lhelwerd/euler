"""
Unit tests for palindromes.
"""

import unittest
from Euler.palindrome import generate, is_palindrome

class PalindromeTest(unittest.TestCase):
    """
    Tests for the palindrome module.
    """

    def test_generate(self) -> None:
        """
        Test the generator providing palindromes.
        """

        palindromes = list(generate(100))
        expected = {
            1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99
        }
        self.assertEqual(set(palindromes), expected)
        # No duplicates
        self.assertEqual(len(palindromes), len(expected))

        longer = list(generate(int(1e5)))
        self.assertIn(2112, longer)
        self.assertEqual(len(longer), len(set(longer)))

    def test_is_palindrome(self) -> None:
        """
        Test the palindrome check.
        """

        self.assertTrue(is_palindrome('2112'))
        self.assertFalse(is_palindrome('25062'))
