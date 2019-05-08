# Finding prime numbers using the Sieve of Eratosthenes

import random
from itertools import chain, product
from past.builtins import xrange as range
from sortedcontainers import SortedSet

class PrimeSet(object):
    def __init__(self, limit, extendable=True, miller=0):
        self.primes = SortedSet([2])
        self.start = 3
        self.limit = 3
        self.extendable = extendable
        self.miller = miller
        self.extend(limit)

    def __iter__(self):
        return iter(self.primes)

    def __reversed__(self):
        return reversed(self.primes)

    def __len__(self):
        return len(self.primes)

    def __getitem__(self, index):
        return self.primes[index]

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
        if self.extendable or num <= self.limit:
            p = num in self.primes
            if p or num <= self.limit:
                return p

            if self.extendable and num <= self.limit * 10:
                self.extend(self.limit * 10)
                return num in self.primes

        if self.miller:
            prime = self.miller_test(num, self.miller)
            if prime:
                self.primes.add(num)

            return prime

        # Find if there are any proper divisors of n (excluding 1 and n) by
        # only using the prime numbers we know and any odd numbers over it that 
        # may be a divisor as well (up to n/2).
        for i in chain(self.primes, self.odd_range(self.limit, num // 2)):
            if num % i == 0:
                return False

        self.primes.add(num)
        return True

    def miller_test(self, n, k):
        # Proper value of k is dependent on the upper bound of n:
        # https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Testing_against_small_sets_of_bases
        p = iter(self.primes)
        r = 0
        d = n - 1
        while d % 2 == 0:
            d //= 2
            r += 1

        # So n = 2^r * d + 1
        for i in range(k):
            a = next(p)
            # Calculate a ^ d mod n
            x = pow(a, d, n)
            if x == 1 or x == n - 1:
                continue

            for j in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                # Composite
                return False

        # For "low" values of n: prime
        return True

    def refresh_limit(self):
        # Consider the set of primes to be complete up to the maximum.
        self.limit = max(self.primes)

    def factorize(self, n):
        p = iter(self.primes)
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

    def proper_divisors(self, n):
        # https://rosettacode.org/wiki/Proper_divisors#Python:_From_prime_factors
        factors = self.factorize(n)
        counts = factors.values()
        multiplicities = product(*(range(count + 1) for count in counts))
        divisors = set()
        for multiplicity in multiplicities:
            d = 1
            for factor, m in zip(factors, multiplicity):
                d *= factor ** m
            if d != n:
                divisors.add(d)

        return divisors

    def totient(self, d, phis):
        if d % 2 == 0:
            phi = 2 * phis[d // 2] if d % 4 == 0 else phis[d // 2]
        else:
            i = 0
            for p in self.primes:
                if d % p == 0:
                    n = d // p
                    phi = phis[n] * ((((n + p - 1) % p) // (p - 1)) + p - 1)
                    break

                if i == self.miller * 2 and d in self:
                    phi = d - 1
                    break

                i += 1

        phis.append(phi)
        return phi
