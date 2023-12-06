"""
Unit tests for finding prime numbers using various algorithms.
"""

import unittest
from Euler.prime import PrimeSet, CoprimeSet

class PrimeTest(unittest.TestCase):
    """
    Tests for the prime module's PrimeSet class.
    """

    def setUp(self) -> None:
        self.prime = PrimeSet(10)

    def test_iter(self) -> None:
        """
        Test the prime set iterator.
        """

        self.assertEqual(list(self.prime), [2, 3, 5, 7])

    def test_reversed(self) -> None:
        """
        Test the prime set reversed iterator.
        """

        self.assertEqual(list(reversed(self.prime)), [7, 5, 3, 2])

    def test_length(self) -> None:
        """
        Test the prime set length.
        """

        self.assertEqual(len(self.prime), 4)

    def test_get(self) -> None:
        """
        Test the prime set item getter.
        """

        self.assertEqual(self.prime[3], 7)
        self.assertEqual(self.prime[1:3], [3, 5])

    def test_range(self) -> None:
        """
        Test the prime set range.
        """

        self.assertEqual(list(self.prime.range(0, 3, reverse=True)), [3, 2])

    def test_extend(self) -> None:
        """
        Test the prime set extension.
        """

        self.prime.extend(20)
        self.assertEqual(list(self.prime), [2, 3, 5, 7, 11, 13, 17, 19])
        # Nothing happens if the extension is lower than current limit
        self.prime.extend(10)
        self.assertEqual(len(self.prime), 8)

    def test_contains(self) -> None:
        """
        Test the prime set contains number check.
        """

        self.assertIn(7, self.prime)
        self.assertNotIn(4, self.prime)
        self.assertIn(23, self.prime)
        self.assertNotIn(25, self.prime)
        # Extendable, but far away from current limit, so divisor test
        self.assertNotIn(10000, self.prime)

        # Miller test
        miller = PrimeSet(10, extendable=False, miller=2)
        self.assertIn(67, miller)
        self.assertNotIn(68, miller)

        # Non-extendable with divisor test
        fixed = PrimeSet(10, extendable=False)
        self.assertIn(13, fixed)
        self.assertNotIn(121, fixed)

    def test_miller_test(self) -> None:
        """
        Test the Miller test.
        """

        self.assertTrue(self.prime.miller_test(67, 2))
        self.assertFalse(self.prime.miller_test(68, 2))
        self.assertFalse(self.prime.miller_test(69, 2))
        self.assertTrue(self.prime.miller_test(73, 2))

    def test_refresh_limit(self) -> None:
        """
        Test the limit refresh after completing set of primes.
        """

        # Normally, this just sets the limit to the maximum prime
        self.prime.refresh_limit()
        self.assertEqual(self.prime.limit, 7)

        # Use case of finding additional primes through other methods
        fixed = PrimeSet(10, extendable=False)
        self.assertIn(11, fixed)
        fixed.refresh_limit()
        self.assertEqual(fixed.limit, 11)

    def test_factorize(self):
        """
        Test the prime-based factorization.
        """

        self.assertEqual(self.prime.factorize(8), {2: 3})
        self.assertEqual(self.prime.factorize(14), {2: 1, 7: 1})
        self.assertEqual(self.prime.factorize(5), {5: 1})
        self.assertEqual(self.prime.factorize(1), {})

    def test_proper_divisors(self) -> None:
        """
        Test the prime-based proper divisor calculation.
        """

        self.assertEqual(self.prime.proper_divisors(8), {1, 2, 4})
        self.assertEqual(self.prime.proper_divisors(14), {1, 2, 7})
        self.assertEqual(self.prime.proper_divisors(5), {1})

    def test_totient(self) -> None:
        """
        Test the totient function.
        """

        phis = [0, 1]
        self.assertEqual(self.prime.totient(2, phis), 1)
        self.assertEqual(self.prime.totient(3, phis), 2)
        self.assertEqual(self.prime.totient(4, phis), 2)
        self.assertEqual(self.prime.totient(5, phis), 4)
        self.assertEqual(self.prime.totient(6, phis), 2)
        self.assertEqual(self.prime.totient(7, phis), 6)
        self.assertEqual(self.prime.totient(8, phis), 4)
        self.assertEqual(self.prime.totient(9, phis), 6)
        self.assertEqual(self.prime.totient(10, phis), 4)
        self.assertEqual(phis, [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4])

        limited = PrimeSet(0, extendable=False)
        with self.assertRaises(ValueError):
            limited.totient(11, phis)

        miller = PrimeSet(10, extendable=False, miller=1)
        self.assertEqual(miller.totient(11, phis), 10)

class CoprimeTest(unittest.TestCase):
    """
    Tests for the prime module's CoprimeSet class.
    """

    def setUp(self) -> None:
        self.coprime = CoprimeSet(5)

    def test_iter(self) -> None:
        """
        Test the coprime set iterator.
        """

        self.assertEqual(list(self.coprime), [(2, 1), (3, 1), (3, 2), (4, 1)])
        longer = CoprimeSet(7)
        self.assertEqual(list(longer), [
            (2, 1), (3, 1), (3, 2), (5, 2), (4, 1), (5, 1), (4, 3), (6, 1)
        ])

    def test_next(self) -> None:
        """
        Test the coprime set next generator.
        """

        self.assertEqual(next(self.coprime), (2, 1))
        self.assertEqual(next(self.coprime), (3, 1))
        self.assertEqual(next(self.coprime), (3, 2))
        self.assertEqual(next(self.coprime), (4, 1))
        with self.assertRaises(StopIteration):
            next(self.coprime)
