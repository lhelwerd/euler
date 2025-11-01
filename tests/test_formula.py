"""
Unit tests for generating sequences of numbers by a formula.
"""

import unittest
from typing import cast, final
from typing_extensions import override

from Euler.formula import Formula, FormulaSet


@final
class FormulaTest(unittest.TestCase):
    """
    Tests for the formula module.
    """

    @override
    def setUp(self) -> None:
        self.formula = FormulaSet(
            cast(Formula, lambda n: n + 1),
            lambda num: int(num) - 1,
            5,
        )

    def test_iter(self) -> None:
        """
        Test the formula set iterator.
        """

        self.assertEqual(list(self.formula), [2, 3, 4, 5, 6])

    def test_length(self) -> None:
        """
        Test the formula set length.
        """

        self.assertEqual(len(self.formula), 5)

    def test_reversed(self) -> None:
        """
        Test the formula set reversed iterator.
        """

        self.assertEqual(list(reversed(self.formula)), [6, 5, 4, 3, 2])

    def test_get(self) -> None:
        """
        Test the formula set item getter.
        """

        self.assertEqual(self.formula[0], 2)
        self.assertEqual(self.formula[1:4], [3, 4, 5])
        self.assertEqual(self.formula[5], 7)
        self.assertEqual(self.formula[10], 12)

    def test_extend(self) -> None:
        """
        Test the formula set extension.
        """

        # Same length causes no change
        self.formula.extend(3)
        self.assertEqual(len(self.formula), 5)

        self.formula.extend(10)
        self.assertEqual(len(self.formula), 10)

    def test_contains(self) -> None:
        """
        Test the formula set contains number check.
        """

        self.assertIn(6, self.formula)
        self.assertNotIn(1, self.formula)
        self.assertIn(7.0, self.formula)
        self.assertIn(12, self.formula)

        index = FormulaSet(
            cast(Formula, lambda n: n * 2.0), lambda num: num / 2, 5
        )
        self.assertIn(4.0, index)
        self.assertIn(16.0, index)
        self.assertNotIn(17.0, index)
