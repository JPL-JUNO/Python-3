"""
@File         : list_set_and_dictionary_comprehensions.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-05-02 00:07:23
@Email        : cuixuanstephen@gmail.com
@Description  : 列表、Set 与字典解析式
"""

nums = [1, 2, 3, 4, 5]
squares = []
for n in nums:
    squares.append(n * n)

squares = [n * n for n in nums]

squares = [n * n for n in nums if n > 2]
portfolio = [
    {"name": "IBM", "shares": 100, "price": 91.1},
    {"name": "MSFT", "shares": 50, "price": 45.67},
    {"name": "HPE", "shares": 75, "price": 34.51},
    {"name": "CAT", "shares": 60, "price": 67.89},
    {"name": "IBM", "shares": 200, "price": 95.25},
]

names = [s["name"] for s in portfolio]

more100 = [s["name"] for s in portfolio if s["shares"] > 100]

cost = sum([s["shares"] * s["price"] for s in portfolio])

names_shares = [(s["name"], s["shares"]) for s in portfolio]

x = 42
squares = [x * x for x in [1, 2, 3]]
squares
x

names = {s["name"] for s in portfolio}
names

prices = {s["name"]: s["price"] for s in portfolio}
prices


def to_int(x):
    try:
        return int(x)
    except ValueError:
        return None


values = ["1", "2", "-4", "n/a", "-3", "5"]
data1 = [to_int(x) for x in values]
data1
# 需要两次调用函数
data2 = [to_int(x) for x in values if to_int(x) is not None]
data2

data3 = [v for x in values if (v := to_int(x)) is not None]
data3
data4 = [v for x in values if (v := to_int(x)) is not None and v >= 0]
data4
