# Functions for converting Roman numerals

from sortedcontainers import SortedDict

values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

minimals = SortedDict([
    (1, ('I', 0)),
    (5, ('V', 1)),
    (10, ('X', 1)),
    (50, ('L', 10)),
    (100, ('C', 10)),
    (500, ('D', 100)),
    (1000, ('M', 100))
])

def to_number(numeral):
    count = 0
    previous = 0
    for d in numeral[::-1]:
        if values[d] < previous:
            count -= values[d]
        else:
            count += values[d]
            previous = values[d]

    return count

def to_roman(number):
    v = list(reversed(minimals))
    i = 0
    numeral = ""
    while number > 0:
        if number >= v[i]:
            number -= v[i]
            numeral += minimals[v[i]][0]
        elif number >= v[i] - minimals[v[i]][1]:
            number -= v[i] - minimals[v[i]][1]
            numeral += minimals[minimals[v[i]][1]][0] + minimals[v[i]][0]
        else:
            i += 1

    return numeral
