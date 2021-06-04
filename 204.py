"""
PROBLEM:     204
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 3
EXPLANATION:
    Number of generalized Hamming numbers of type 100 (with no prime factor
    larger than 100) below 10 ** 9
"""

import timeit
from Euler.prime import PrimeSet

# https://github.com/python/cpython/blob/main/Lib/test/test_generators.py#L1007
def times(n, generator):
    for i in generator:
        yield n * i

def merge(*generators):
    yield 1
    values = [next(gen) for gen in generators]
    n = None
    while True:
        m = min(values)
        i = values.index(m)
        if m != n:
            yield m
            n = m

        # Must be called after enough has been yielded, otherwise the lazy 
        # storage will not contain enough to collect from
        values[i] = next(generators[i])

class LazyList(object):
    def __init__(self):
        self.collected = []
        self.fetch = None

    def set_generator(self, generator):
        self.fetch = generator.__next__

    def __getitem__(self, i):
        while i >= len(self.collected):
            self.collected.append(self.fetch())

        return self.collected[i]

def problem():
    hamming = 100 # 5
    limit = 10 ** 9 # 10 ** 8
    primes = PrimeSet(hamming)
    storage = LazyList()
    generators = [times(p, storage) for p in primes]
    storage.set_generator(merge(*generators))

    i = 0
    while storage[i] <= limit:
        i += 1

    print(i)

if __name__ == "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))
