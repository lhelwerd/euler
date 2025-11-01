"""
Triangle file reading and operations.
"""

from os import PathLike
from pathlib import Path


def path(filename: str | PathLike[str]) -> int:
    """
    Read a triangle file and find the maximum path sum in it.
    """

    triangle: list[list[int]] = []
    paths: list[list[int]] = []
    with Path(filename).open("r", encoding="utf-8") as numbers:
        for line in numbers:
            cols = line.strip().split(" ")
            triangle.append([int(c) for c in cols])
            paths.append([0] * len(cols))

    paths[0][0] = triangle[0][0]

    row = 0
    for row in range(1, len(triangle)):
        end = len(paths[row - 1])
        paths[row] = [
            triangle[row][i]
            + max(
                paths[row - 1][i - 1] if i > 0 else 0,
                paths[row - 1][i] if i < end else 0,
            )
            for i in range(len(triangle[row]))
        ]

    return max(paths[row])
