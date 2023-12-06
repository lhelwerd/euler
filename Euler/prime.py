"""
Module for finding prime numbers using various algorithms.
"""

from collections import deque
from itertools import chain, product
from typing import overload, Dict, Iterator, List, Sequence, Set, Tuple
from sortedcontainers import SortedSet

class PrimeSet:
    """
    Collection of prime numbers that should have no proper divisors except 1.
    """

    def __init__(self, limit: int, extendable: bool = True, miller: int = 0):
        self.primes = SortedSet([2])
        self.start = 3
        self.limit = 3
        self.extendable = extendable
        self.miller = miller
        self.extend(limit)

    def __iter__(self) -> Iterator[int]:
        return iter(self.primes)

    def __reversed__(self) -> Iterator[int]:
        return reversed(self.primes)

    def __len__(self) -> int:
        return len(self.primes)

    @overload
    def __getitem__(self, item: slice) -> Sequence[int]: ...
    @overload
    def __getitem__(self, item: int) -> int: ...
    def __getitem__(self, item):
        return self.primes[item]

    @staticmethod
    def _odd_range(start: int, limit: int) -> 'range':
        return range(2 * (start // 2) + 1, limit, 2)

    def range(self, start: int, limit: int, reverse: bool = False) \
            -> Iterator[int]:
        """
        Retrieve a range of known prime numbers.
        """

        return self.primes.irange(start, limit, reverse=reverse)

    def extend(self, limit: int) -> None:
        """
        Increase the sequence of generated primes to go up to `limit`, a number
        which may or may not be prime itself.
        """

        if limit < self.start:
            return

        maxbase = int(limit**0.5) + 1
        self.extend(maxbase)
        self.limit = limit
        # All odd numbers are candidate primes
        self.start = self.primes[-1] + 1
        self.primes.update(self._odd_range(self.start, self.limit + 1))

        # Remove non-primes based on earlier found numbers
        for prime in self.range(3, maxbase):
            start_prime = self.start + prime - (self.start % prime)
            self.primes.difference_update(range(start_prime, self.limit + 1,
                                                prime))

    def __contains__(self, number: int) -> bool:
        if self.extendable or number <= self.limit:
            is_prime = number in self.primes
            if is_prime or number <= self.limit:
                return is_prime

            if self.extendable and number <= self.limit * 10:
                self.extend(self.limit * 10)
                return number in self.primes

        if self.miller:
            is_prime = self.miller_test(number, self.miller)
            if is_prime:
                self.primes.add(number)

            return is_prime

        # Find if there are any proper divisors of n (excluding 1 and n) by
        # only using the prime numbers we know and any odd numbers over it that
        # may be a divisor as well (up to n/2).
        for divisor in chain(self.primes,
                             self._odd_range(self.limit, number // 2)):
            if number % divisor == 0:
                return False

        self.primes.add(number)
        return True

    def miller_test(self, number: int, base: int) -> bool:
        """
        Perform the Miller test on number `n` with base `k`.

        Proper value of `k` is dependent on the upper bound of `n`:
        https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
        """

        primes = iter(self.primes)
        power = 0
        odd = number - 1
        while odd % 2 == 0:
            odd //= 2
            power += 1

        # So n = 2^r * d + 1
        for _ in range(base):
            prime = next(primes)
            # Calculate a ^ d mod n
            poly = pow(prime, odd, number)
            if poly in (1, number - 1):
                continue

            for _ in range(power - 1):
                poly = pow(poly, 2, number)
                if poly == number - 1:
                    break
            else:
                # Composite
                return False

        # For "low" values of n: prime
        return True

    def refresh_limit(self) -> None:
        """
        Consider the set of primes to be complete up to the maximum number.
        """

        self.limit = max(self.primes)

    def factorize(self, number: int) -> Dict[int, int]:
        """
        Factorize the number `n` into a dictionary of prime numbers and their
        products.
        """

        primes = iter(self.primes)
        prime = next(primes)
        factors = {}
        factor = 0

        while prime * prime <= number:
            if number % prime == 0:
                factor += 1
                number //= prime
            else:
                if factor != 0:
                    factors[prime] = factor
                    factor = 0
                prime = next(primes)

        if factor != 0:
            factors[prime] = factor
        if number > 1:
            factors.setdefault(number, 0)
            factors[number] += 1

        return factors

    def proper_divisors(self, number: int) -> Set[int]:
        """
        Calculate the proper divisors of `number` using known prime numbers.

        https://rosettacode.org/wiki/Proper_divisors#Python:_From_prime_factors
        """

        factors = self.factorize(number)
        counts = factors.values()
        multiplicities = product(*(range(count + 1) for count in counts))
        divisors = set()
        for multiplicity in multiplicities:
            divisor = 1
            for factor, power in zip(factors, multiplicity):
                divisor *= factor ** power
            if divisor != number:
                divisors.add(divisor)

        return divisors

    def totient(self, number: int, phis: List[int]) -> int:
        """
        Calculate a value of Euler's totient or phi function for input `number`
        and store the totient in a list `phis`.
        """

        if number % 2 == 0:
            if number % 4 == 0:
                phi = 2 * phis[number // 2]
            else:
                phi = phis[number // 2]
        else:
            step = 0
            for prime in self.primes:
                if number % prime == 0:
                    factor = number // prime
                    phi = phis[factor] * (
                        (((factor + prime - 1) % prime) // (prime - 1)) + \
                        prime - 1
                    )
                    break

                if step == self.miller * 2 and number in self:
                    phi = number - 1
                    break

                step += 1

        phis.append(phi)
        return phi

class CoprimeSet:
    """
    A sequence of pairs of coprime numbers.
    """

    def __init__(self, limit: int):
        self.limit = limit
        self.children = [(2, 1), (3, 1)]
        self.candidates = deque(self.children)

    def __iter__(self) -> Iterator[Tuple[int, int]]:
        return self

    def __next__(self) -> Tuple[int, int]:
        while not self.children:
            if not self.candidates:
                raise StopIteration

            candidate = self.candidates.popleft()
            if 2 * candidate[0] - candidate[1] + candidate[0] <= self.limit:
                self.children.append((2 * candidate[0] - candidate[1],
                                      candidate[0]))
            if 2 * candidate[0] + candidate[1] + candidate[0] <= self.limit:
                self.children.append((2 * candidate[0] + candidate[1],
                                      candidate[0]))
            if candidate[0] + 2 * candidate[1] + candidate[1] <= self.limit:
                self.children.append((candidate[0] + 2 * candidate[1],
                                      candidate[1]))

            self.candidates.extend(self.children)

        return self.children.pop(0)
