"""
@Description: Python Refresher
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-04 10:36:42
"""

x, y = 3, 2
assert x + y == 5
assert x - y == 1
assert x * y == 6
assert x / y == 1.5
assert x // y == 1
assert x % y == 1
assert -x == -3
assert abs(-x) == 3
assert int(3.9) == 3
assert float(x) == 3.0
assert x ** y == 9


# Booleans
x = 1 > 2
assert x == False
y = 2 > 1
assert y == True

x, y = True, False
assert x or y == True
assert x and y == False
assert not y == True

x, y = True, False
assert x and not y == True
assert not x and y or x == True

if None or 0 or 0.0 or '' or [] or {} or set():
    print("Dead code")

# strings
y = "   this is lazy \t\n"
assert y.strip() == "this is lazy"
assert "DrDre".lower() == "drdre"
assert "attention".upper() == 'ATTENTION'
assert "smartphone".startswith("smart")
assert "smartphone".endswith("phone")
assert "another".find("other") == 2
assert "cheat".replace("ch", "m") == "meat"
assert ",".join(["F", "B", "I"]) == "F,B,I"
assert len('abcd') == 4
assert "ear" in "earth"


def f():
    x = 2


assert f() is None
assert "" != None
assert 0 != None

# Container Data Structures
# Lists
l = [1, 2, 2]
assert len(l) == 3

y = x = 3
assert x is y

assert [3] is not [3]

# adding elements
l = [2, 2, 2]
l.append(4)
assert l == [2, 2, 2, 4]

l = [1, 2, 4]
l.insert(2, 3)
assert l == [1, 2, 3, 4]

assert [1, 2, 3] + [4] == [1, 2, 3, 4]

# removing elements
l = [1, 2, 2, 4]
l.remove(1)
assert l == [2, 2, 4]

# reserve elements
l = [1, 2, 2, 4]
l.reverse()
assert l == [4, 2, 2, 1]

# sorting lists
l = [2, 1, 4, 2]
l.sort()
assert l == [1, 2, 2, 4]

# indexing list elements
assert [2, 2, 4].index(2) == 0
assert [2, 2, 4].index(2, 1) == 1

# stacks
stack = [3]
stack.append(42)
stack.pop()
assert stack == [3]
stack.pop()
assert stack == []

# collection
hero = "Harry"
guide = "Dumbledore"
enemy = "Lord V."
print(hash(hero))
print(hash(guide))
characters = {hero, guide, enemy}
assert characters == {"Harry", "Dumbledore", "Lord V."}

team_1 = [hero, guide]
team_2 = [enemy]
try:
    teams = {team_1, team_2}
except TypeError as e:
    print(e.args[0])

print(characters)
# Dictionaries
calories = {'apple': 52, 'banana': 89, 'chocolate': 546}
assert calories['apple'] < calories["banana"]
calories['cappu'] = 74
calories['banana'] < calories['cappu']
assert 'apple' in calories.keys()
assert 52 in calories.values()

for k, v in calories.items():
    print(k) if v > 500 else None

# Membership
assert 42 in [2, 39, 42]
assert '21' not in {'2', '39', '42'}
assert 'list' in {"list": [1, 2, 3], "set": {1, 2, 3}}


# List and Set Comprehension
customers = [("John", 240000),
             ("Alice", 120000),
             ("Ann", 1100000),
             ("Zach", 44000)]
whales = [x for x, y in customers if y > 1_000_000]

assert whales == ['Ann']


def appreciate(x, percentage) -> float:
    return x + x * percentage / 100


# lambda function
assert (lambda x: x + 3)(3) == 6
# First, you create a lambda function that takes a value x and returns
# the result of the expression x + 3. The result is a function object that can
# be called like any other function.
