"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-10 13:12:23
@Description: 
"""

from typing import NamedTuple
import typing


class Coordinate(NamedTuple):
    lat: float
    lon: float

    def __str__(self) -> str:
        ns = "N" if self.lat >= 0 else "S"
        we = "E" if self.lon >= 0 else "W"
        return f"{abs(self.lat):.1f}°{ns}, {abs(self.lon):.1f}°{we}"


# assert not issubclass(Coordinate, typing.NamedTuple)
assert issubclass(Coordinate, tuple)
