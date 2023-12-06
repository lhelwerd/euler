"""
Unit tests for modular arithmetic.
"""

import unittest
from Euler.modulo import inverse

class ModuloTest(unittest.TestCase):
    """
    Tests for the modulo module.
    """

    def test_inverse(self) -> None:
        """
        Test the multiplicative modular inverse.
        """

        self.assertEqual(inverse(3, 4), 3)
        self.assertEqual(inverse(4, 9), 7)
        self.assertEqual(inverse(5, 16), 13)
        self.assertEqual(inverse(2, 4), 0)
        self.assertEqual(inverse(4, 3), 1)
