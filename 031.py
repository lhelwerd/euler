"""
PROBLEM:     031
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Coin sums with recursion and pruning
"""

import timeit

# All coins that can divide the later coins
divisors = set((5, 10, 50, 100))

def count(coin_sum, options):
    # End conditions
    if coin_sum == 200:
        return 1
    elif coin_sum > 200:
        return 0

    # Stop searching in a tree that cannot be totalled to exactly 200p, i.e.,
    # if we choose an option that causes us to not be able to add 1p or 2p or 
    # other coins to get to the total.
    if options[0] in divisors and (200 - coin_sum) % options[0] != 0:
        return 0

    # Never go for an earlier coin option once we choose one
    num = 0
    for i, option in enumerate(options):
        num += count(coin_sum + option, options[i:])

    return num

def problem():
    # 200 is just one option so just count it separately.
    print(count(0, (1, 2, 5, 10, 20, 50, 100)) + 1)


if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

