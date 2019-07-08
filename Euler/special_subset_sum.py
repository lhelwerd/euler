"""
Special subset sum set properties.
"""

import itertools

def special_subset_sum_set(candidate):
    """
    Test if a candidate set conforms to the special subset sum property.
    """

    a = set(candidate)
    for r in range(1, len(a) // 2 + 2):
        for comb in itertools.combinations(a, r):
            b = set(comb)
            rest = a - b
            for q in range(1, len(rest) + 1):
                for comb2 in itertools.combinations(rest, q):
                    c = set(comb2)
                    if sum(b) == sum(c):
                        return False
                    if len(b) > len(c) and sum(b) < sum(c):
                        return False

    return True
