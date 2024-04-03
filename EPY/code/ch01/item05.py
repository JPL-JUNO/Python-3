"""
@File  : item05.py
@Author: Stephen CUI
@Time  : 2024-01-02 15:23:41
"""

from urllib.parse import parse_qs

my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)

print(repr(my_values))

print("Red    :", my_values.get("red"))
print("Blue   :", my_values.get("blue"))
print("Opacity:", my_values.get("opacity"))

# 需求：把缺失的值或者空白值变为 0
red = my_values.get("red", [""])[0] or 0
green = my_values.get("green", [""])[0] or 0
opacity = my_values.get("opacity", [""])[0] or 0
print(f"Red     : {red!r}")
print(f"Green   : {green!r}")
print(f"Opacity : {opacity!r}")
# 这样的写法在于很丑


red_str = my_values.get("red", [""])
red = int(red_str[0]) if red_str[0] else 0

green_str = my_values.get("green", [""])
if green_str[0]:
    green = int(green_str[0])
else:
    green = 0


def get_first_int(values, key, default: int = 0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    else:
        return default
    #  return int(found[0]) if found[0] else 0
