"""
@Title: 对不支持原生比较操作的对象排序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 14:24:18
@Description: 
"""


class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self) -> str:
        return "User({})".format(self.user_id)


users = [User(23), User(3), User(2), User(99)]
sorted(users, key=lambda u: u.user_id)

from operator import attrgetter
sorted(users, key=attrgetter("user_id"))

# by_name = sorted(users, key=attrgetter("last_name", "first_name"))

min(users, key=attrgetter("user_id"))
max(users, key=attrgetter("user_id"))
