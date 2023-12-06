"""
Unit tests for text file reading.
"""

import unittest
from Euler.text import read

class TextTest(unittest.TestCase):
    """
    Tests for the text module.
    """

    def test_read(self) -> None:
        """
        Test the large file reader.
        """

        self.assertEqual(len(read('tests/text.txt')), 200)
