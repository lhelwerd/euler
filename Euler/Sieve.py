# Sieve of Eratosthenes

from builtins import range
from collections import OrderedDict
import json
import os.path

def Sieve(num):
    if os.path.exists('sieve.json'):
        with open('sieve.json', 'r') as sieve:
            return set(json.load(sieve))

    nonprimes = set()
    primes = set()
    for i in range(2, num):
        if i not in nonprimes:
            primes.add(i)
            for j in range(i * 2, num, i):
                nonprimes.add(j)
        else:
            # Save memory
            nonprimes.remove(i)

    with open('sieve.json', 'w') as sieve:
        json.dump(list(sorted(primes)), sieve)

    return primes
