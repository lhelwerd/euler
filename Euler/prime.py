# Finding prime numbers using the Sieve of Eratosthenes

from builtins import range
from itertools import chain
from sortedcontainers import SortedSet

class PrimeSet(object):
    def __init__(self, limit, extendable=True):
        self.primes = SortedSet([2])
        self.start = 3
        self.limit = 3
        self.extendable = extendable
        self.extend(limit)

    def __iter__(self):
        return iter(self.primes)

    def __reversed__(self):
        return reversed(self.primes)

    @staticmethod
    def odd_range(start, limit):
        return range(2 * (start // 2) + 1, limit, 2)

    def extend(self, limit):
        if limit <= self.start:
            return

        self.start = self.limit
        self.limit = limit
        # All odd numbers are candidate primes
        self.primes.update(self.odd_range(self.start, self.limit))

        # Remove non-primes based on earlier found numbers
        for p in self.odd_range(3, self.start):
            if p in self.primes:
                start_p = self.start + p - (self.start % p)
                self.primes.difference_update(range(start_p, self.limit + 1, p))

        for i in range(self.start, self.limit, 2):
            if i in self.primes:
                self.primes.difference_update(range(i * 2, self.limit + 1, i))

    def __contains__(self, num):
        if num <= self.limit:
            return num in self.primes
        if num <= self.limit * 10 and self.extendable:
            self.extend(self.limit * 10)
            return num in self.primes

        # Find if there are any proper divisors of n (excluding 1 and n) by
        # only using the prime numbers we know and any odd numbers over it that 
        # may be a divisor as well (up to n/2).
        for i in chain(self.primes, self.odd_range(self.limit, num)):
            if num % i == 0:
                return False

        return True

    def factorize(self, n):
        p = iter(self)
        j = next(p)
        factors = {}
        factor = 0

        while j * j <= n:
            if n % j == 0:
                factor += 1
                n //= j
            else:
                if factor != 0:
                    factors[j] = factor
                    factor = 0
                j = next(p)

        if factor != 0:
            factors[j] = factor
        if n > 1 and n % j != 0:
            factors[n] = 1

        return factors
