"""
Unit tests for special subset sum set properties.
"""

import unittest
from Euler.special_subset_sum import special_subset_sum_set

class SpecialSubsetSumTest(unittest.TestCase):
    """
    Tests for the special subset sum module.
    """

    def test_special_subset_sum_set(self) -> None:
        """
        Test the special subset sum property check.
        """

        self.assertTrue(special_subset_sum_set([1]))
        self.assertTrue(special_subset_sum_set((1, 2)))
        self.assertTrue(special_subset_sum_set({2, 3, 4}))
        self.assertTrue(special_subset_sum_set({6, 9, 11, 12, 13}))
