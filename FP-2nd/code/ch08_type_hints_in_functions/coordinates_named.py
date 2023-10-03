"""
@Title: 带有举名字段，用作记录的元组
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 18:09:00
@Description: 
"""

from typing import NamedTuple
from geolib import geohash as gh

PRECISION = 9


class Coordinate(NamedTuple):
    lat: float
    lon: float


def geohash(lat_lon: Coordinate) -> str:
    return gh.geohash(*lat_lon, PRECISION)
