"""
Unit tests for triangle file reading and operations.
"""

import unittest
from Euler.triangle import path

class TriangleTest(unittest.TestCase):
    """
    Tests for the triangle  module.
    """

    def test_path(self) -> None:
        """
        Test the triangle file reader and maximum path sum.
        """

        self.assertEqual(path('tests/triangle.txt'), 23)
