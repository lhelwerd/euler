"""
Module for converting Roman numerals.
"""

from sortedcontainers import SortedDict

VALUES: dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

MINIMALS: SortedDict[int, tuple[str, int]] = SortedDict(
    [
        (1, ("I", 0)),
        (5, ("V", 1)),
        (10, ("X", 1)),
        (50, ("L", 10)),
        (100, ("C", 10)),
        (500, ("D", 100)),
        (1000, ("M", 100)),
    ]
)


def to_number(numeral: str) -> int:
    """
    Convert a Roman `numeral` to its numeric representation.
    """

    count = 0
    previous = 0
    for letter in numeral[::-1]:
        if VALUES[letter] < previous:
            count -= VALUES[letter]
        else:
            count += VALUES[letter]
            previous = VALUES[letter]

    return count


def to_roman(number: int) -> str:
    """
    Convert the `number` to Roman numeral representation.
    """

    values = list(reversed(MINIMALS))
    index = 0
    numeral = ""
    while number > 0:
        if number >= values[index]:
            number -= values[index]
            numeral += MINIMALS[values[index]][0]
        elif number >= values[index] - MINIMALS[values[index]][1]:
            number -= values[index] - MINIMALS[values[index]][1]
            numeral += (
                MINIMALS[MINIMALS[values[index]][1]][0]
                + MINIMALS[values[index]][0]
            )
        else:
            index += 1

    return numeral
