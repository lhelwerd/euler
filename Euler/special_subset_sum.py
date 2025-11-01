"""
Special subset sum set properties.
"""

import itertools
from collections.abc import Collection


def special_subset_sum_set(candidate: Collection[int]) -> bool:
    """
    Test if a candidate set conforms to the special subset sum property.
    """

    candidate = set(candidate)
    for length in range(1, len(candidate) // 2 + 2):
        for comb in itertools.combinations(candidate, length):
            rest = candidate - set(comb)
            for rest_length in range(1, len(rest) + 1):
                for comb2 in itertools.combinations(rest, rest_length):
                    if sum(comb) == sum(comb2):
                        return False
                    if len(comb) > len(comb2) and sum(comb) < sum(comb2):
                        return False

    return True
