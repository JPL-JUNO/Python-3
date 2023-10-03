"""
@Title: 用作记录的元组
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-03 18:05:04
@Description: 
"""

# 这个注释会禁止 mypy 报告 geolib 包没有类型提示
from geolib import geohash as gh  # type: ignore

PRECISION = 9


def geohash(lat_lon: tuple[float, float]) -> str:
    return gh.encode(*lat_lon, PRECISION)
