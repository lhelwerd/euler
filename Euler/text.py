"""
Text file reading.
"""

from os import PathLike
from typing import Callable, List, Union

def read(filename: Union[str, PathLike[str]],
         reducer: Callable[[List[str], str], None] = \
                 lambda result, word: result.append(word)) -> List[str]:
    """
    Read the (potentially large) file containing words between double quotes.
    The reading is kept more efficiently through buffering, while a `reducer`
    is called to perform operations on the list while creating it, for example
    for sorting.
    """

    result: List[str] = []
    word = ""
    buffered = 'initial'
    in_word = False

    with open(filename, 'r', encoding='utf-8') as words:
        while buffered:
            buffered = words.read(1024)
            j = 0
            i = buffered.find("\"")
            while i != -1:
                if in_word:
                    word += buffered[j:i]

                if word != "":
                    reducer(result, word)
                    in_word = False
                else:
                    in_word = j == 0
                    j = i + 1

                if not in_word:
                    # Next open
                    i = buffered.find("\"", i + 1)
                    j = i + 1
                    in_word = i != -1

                if i != -1:
                    # Next close
                    i = buffered.find("\"", i + 1)

                word = ""

            if j > 0:
                word = buffered[j:]

    return result
