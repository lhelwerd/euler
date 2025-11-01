"""
Text file reading.
"""

from collections.abc import Callable
from os import PathLike
from pathlib import Path


def _handle_buffer(
    buffer: str,
    result: list[str],
    reducer: Callable[[list[str], str], None] = (
        lambda result, word: result.append(word)
    ),
    word: str = "",
    in_word: bool = False,
) -> tuple[str, bool]:
    j = 0
    i = buffer.find('"')
    while i != -1:
        if in_word:
            word += buffer[j:i]

        if word != "":
            reducer(result, word)
            in_word = False
        else:
            in_word = j == 0
            j = i + 1

        if not in_word:
            # Next open
            i = buffer.find('"', i + 1)
            j = i + 1
            in_word = i != -1

        if i != -1:
            # Next close
            i = buffer.find('"', i + 1)

        word = ""

    if j > 0:
        word = buffer[j:]

    return word, in_word


def read(
    filename: str | PathLike[str],
    reducer: Callable[[list[str], str], None] = (
        lambda result, word: result.append(word)
    ),
) -> list[str]:
    """
    Read the (potentially large) file containing words between double quotes.
    The reading is kept more efficiently through buffering, while a `reducer`
    is called to perform operations on the list while creating it, for example
    for sorting.
    """

    result: list[str] = []
    word = ""
    buffered = "initial"
    in_word = False

    with Path(filename).open("r", encoding="utf-8") as words:
        while buffered:
            buffered = words.read(1024)
            word, in_word = _handle_buffer(
                buffered, result, reducer, word, in_word
            )

    return result
