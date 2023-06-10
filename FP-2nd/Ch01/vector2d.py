"""
@Description: 一个简单的二维向量类
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-10 12:47:05
"""

import math
class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self)->float:
        return math.hypot(self.x, self.y)
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x,y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    