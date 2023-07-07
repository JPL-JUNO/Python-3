"""
@Description: enum – A group of constants
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-07 12:31:16
"""
import enum


class Color(enum.Enum):
    """类Color是一个enumeration（或称enum）

    属性Color.red， Color.green等等是枚举成员（或称enum成员）并且被用作常量
    枚举成员有名称和值（例如Color.red的名称为red， color.green的值为2等等
    """
    red = 1
    green = 2
    blue = 3


print(Color.red)
print(Color['red'])
print(Color(1))

print(Color.red.name)
print(Color.red.value)

assert isinstance(Color.red, Color)
assert Color.red is Color['red']
assert Color.red is Color(1)

for color in Color:
    print(color)

colors = dict()
colors[Color.green] = 0x00FF00
print(colors)


class Spam(enum.Enum):
    EGGS = 'eggs'


# 与非枚举值的比较将总是不相等
assert not Spam.EGGS == 'eggs'


class Spam(str, enum.Enum):
    EGGS = 'eggs'


assert Spam.EGGS == 'eggs'

a = enum.Enum({'d': 1})
