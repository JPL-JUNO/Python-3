"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-10 12:50:00
@Description: 
"""


class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


moscow = Coordinate(55.76, 37.62)
location = Coordinate(55.76, 37.62)
# 继承来的__repr__没多大作用
print(moscow)
# 继承来的__eq__比较的是标识（ID）
assert not location == moscow
assert (location.lat, location.lon) == (moscow.lat, moscow.lon)
