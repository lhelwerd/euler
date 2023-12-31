"""
Module for generating sequences of numbers by a formula.
"""

from typing import overload, Callable, Iterator, Protocol, Sequence, Union
import numpy as np
from numpy.typing import NDArray
from sortedcontainers import SortedSet

class Formula(Protocol): # pragma: no cover
    # pylint: disable=too-few-public-methods
    """
    Type specification for formula function.
    """

    @overload
    def __call__(self, number: int) -> float: ...
    @overload
    def __call__(self, number: NDArray[np.int64]) -> NDArray[np.float64]: ...

class FormulaSet:
    """
    An unique collection of numbers generated by expanding a formula.
    """

    def __init__(self, formula: Formula,
                 index: Callable[[float], Union[float, int]], limit: int,
                 extendable: bool = True):
        self.formula = formula
        self.index = index
        self.numbers: SortedSet[float] = SortedSet()
        self.start = 0
        self.limit = 0
        self.maximum = 0.0
        self.extendable = extendable
        self.extend(limit)

    def __iter__(self) -> Iterator[float]:
        return iter(self.numbers)

    def __len__(self) -> int:
        return len(self.numbers)

    def __reversed__(self) -> Iterator[float]:
        return reversed(self.numbers)

    @overload
    def __getitem__(self, item: slice) -> Sequence[float]: ... # pragma: no cover
    @overload
    def __getitem__(self, item: int) -> float: ... # pragma: no cover
    def __getitem__(self, item):
        if not isinstance(item, slice) and item >= self.limit:
            self.extend(item + 1)

        return self.numbers[item]

    def extend(self, limit: int) -> None:
        """
        Increase the sequence of generated numbers to go up to `limit` numbers.
        """

        if limit <= self.limit:
            return

        self.start = self.limit
        self.limit = limit
        self.numbers.update(self.formula(np.array(range(self.start + 1,
                                                        self.limit + 1))))
        self.maximum = float(self.formula(self.limit))

    def __contains__(self, number: float) -> bool:
        if self.extendable and number > self.maximum:
            # Determine which index we require. If the index function returns
            # a float, then it doubles as a membership test in that the number
            # is part of the sequence if and only if the value is a natural
            # number. Otherwise the index must be at least or higher than
            # the index of the number in the sequence.
            index = self.index(number)
            if isinstance(index, float):
                return index == int(index)

            self.extend(index)

        return number in self.numbers
