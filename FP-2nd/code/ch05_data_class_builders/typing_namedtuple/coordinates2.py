"""
@Title: 带类型的具名元组
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-10 13:47:33
@Description: 
"""

from typing import NamedTuple


class Coordinate(NamedTuple):
    lat: float
    lon: float
    reference: str = ["WGS84"]
