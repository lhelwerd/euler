"""
PROBLEM:     022
AUTHOR:      Leon Helwerda
STATUS:      done
INTERPRETER: Python 2 or 3
EXPLANATION:
    Name scores from a list of names after alphabetically ordering them
    The name score of a name is defined as the position of the name in the
    ordered list (starting from 1) times the alphabetical value, calculated
    by the sum of the position in the alphabet of each character in the name.
"""

from bisect import bisect
import timeit

def problem():
    ordered = []
    name = ""
    buffered = True
    in_name = False

    # Read the (potentially large) file efficiently through buffering and sort 
    # the list while creating it.
    with open("p022_names.txt") as names:
        while buffered:
            buffered = names.read(1024)
            j = 0
            i = buffered.find("\"")
            while i != -1:
                if in_name:
                    name += buffered[j:i]

                if name != "":
                    ordered.insert(bisect(ordered, name), name)
                    in_name = False
                else:
                    in_name = j == 0
                    j = i + 1

                if not in_name:
                    # Next open
                    i = buffered.find("\"", i + 1)
                    j = i + 1
                    in_name = i != -1

                if i != -1:
                    # Next close
                    i = buffered.find("\"", i + 1)

                name = ""

            if j > 0:
                name = buffered[j:]

    print(sum((i + 1) * sum(ord(c) - ord('A') + 1 for c in name)
              for (i, name) in enumerate(ordered)))


if __name__== "__main__":
    print(timeit.timeit("problem()", setup="from __main__ import problem",
                        number=1))

