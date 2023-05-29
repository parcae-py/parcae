from __future__ import annotations
from typing import TYPE_CHECKING, AnyStr


if TYPE_CHECKING:
    from typing_extensions import Self

class ParcaeError(Exception):
    def __init__(self: Self, message: AnyStr) -> None:
        super().__init__(message)


class InvalidPyPIName(ParcaeError):
    pass


