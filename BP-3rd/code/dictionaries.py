"""
@File         : Dictionaries.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-07 20:25:59
@Email        : cuixuanstephen@gmail.com
@Description  : 当索引行不通时
"""

d = {}
d["name"] = "Gumby"
d["age"] = 42
d
returned_value = d.clear()
d
assert returned_value is None

x = {}
y = x
x["key"] = "value"
y
x
x = {}
y

x = {}
y = x
x["key"] = "value"
y
x.clear()
y

x = {"user_name": "admin", "machines": ["foo", "bar", "baz"]}
y = x.copy()
y["user_name"] = "mlh"
y["machines"].remove("bar")
y
x

from copy import deepcopy

d = {}
d["names"] = ["Alfred", "Bertrand"]
c = d.copy()
dc = deepcopy(d)
d["names"].append("Clive")
c
dc

{}.fromkeys(["name", "age"])
{}.fromkeys(["name", "age"], "NAN")

dict.fromkeys(["name", "age"])

d = {}
d["name"]
d.get("name")
d.get("name", "NAN")
d["name"] = "Python"
d.get("name")

d = {"Language": "Python", "url": "http://www.python.org", "others": "R"}
d.items()
it = d.items()
len(it)
assert ("others", "R") in it

d["others"] = "ggplot2"
assert ("others", "R") not in it
d["others"] = 0
assert ("others", 0) in it

d = {"x": 1, "language": "Python"}
d.pop("x")
d
d.pop("R")
