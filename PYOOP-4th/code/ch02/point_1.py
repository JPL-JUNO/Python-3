"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-29 21:39:43
@Description: 
"""
import math


class Point:
    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.x = 0
        self.y = 0

    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
