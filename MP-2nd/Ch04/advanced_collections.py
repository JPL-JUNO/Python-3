"""
@Description: Pythonic patterns using advanced collections
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-06 21:07:19
"""

spam: int
print(__annotations__['spam'])

spam = 'not a number'
# even with the int type hint,
# we can still insert a str if we want to
print(__annotations__['spam'])

import dataclasses


@dataclasses.dataclass
class Sandwich:
    spam: int
    eggs: int = 3


print(Sandwich(1, 2))

sandwich = Sandwich(4)
print(sandwich)

print(dataclasses.asdict(sandwich))
print(dataclasses.astuple(sandwich))

# print(help(dataclasses.dataclass))


# def __init__(self, spam, eggs: int = 3):
#     self.spam = spam
#     self.eggs = eggs

import typing


@dataclasses.dataclass
class Group:
    name: str
    parent: 'Group' = None


@dataclasses.dataclass
class User:
    username: str
    email: str = None
    groups: typing.List[Group] = None


users = Group('users')
admins = Group('admins', users)
rick = User('rick', groups=[admins])
gvr = User('gvanrossum', 'guido@python.org', [admins])
print(rick.groups)
print(rick.groups[0].parent)
