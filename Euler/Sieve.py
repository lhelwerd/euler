# Sieve of Eratosthenes

from builtins import range
from collections import OrderedDict
import json
import os.path

def Sieve(num):
    # All odd numbers are candidate primes
    primes = set(range(3, num, 2))
    primes.add(2)
    for i in range(3, num, 2):
        if i in primes:
            primes.difference_update(range(i * 2, num, i))

    return primes
