"""
@File         : item16.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-10 21:53:43
@Email        : cuixuanstephen@gmail.com
@Description  : 用 get 处理键不在字典中的情况，不要使用 in 和 KeyError
"""

counters = {
    "pumpernickel": 2,
    "sourdough": 1,
}

key = "wheat"
if key in counters:
    count = counters[key]
else:
    count = 0
counters[key] = count + 1

try:
    # 获取不存在的键的值时，字典会引发 KeyError 异常。
    count = counters[key]
except KeyError:
    count = 0
counters[key] = count + 1

count = counters.get(key, 0)
counters[count] = count + 1

if key not in counters:
    counters[key] = 0
counters[key] += 1

if key in counters:
    counters[key] += 1
else:
    counters[key] = 1

try:
    counters[key] += 1
except KeyError:
    counters[key] = 1

votes = {
    "baguette": ["Bob", "Alice"],
    "ciabatta": ["Coco", "Deb"],
}
key = "brioche"
who = "Elmer"
if key in votes:
    names = votes[key]
else:
    votes[key] = names = []
names.append(who)
print(votes)

try:
    names = votes[key]
except KeyError:
    votes[key] = names = []
names.append(who)

names = votes.get(key)
if names is None:
    votes[key] = names = []
names.append(who)

if (names := votes.get(key)) is None:
    votes[key] = names = []
names.append(who)

names = votes.setdefault(key, [])
names.append(who)

data = {}
key = "foo"
value = []
data.setdefault(key, value)
print("Before:", data)
value.append("Hello")
print("After:", data)

count = counters.setdefault(key, 0)
counters[key] = count + 1
