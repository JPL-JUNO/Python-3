"""
@Title: overriding and super
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-14 09:19:25
@Description: 
"""

from commerce_v2 import Contact


# class Friend(Contact):
#     def __init__(self,
#                  name: str,
#                  email: str,
#                  phone: str) -> None:
#         self.name = name
#         self.email = email
#         self.phone = phone
#     # 缺点1，有很多的重复代码
#     # 缺点2，没有添加至 all_contacts
#     # 缺点3，如果父类添加新特征，这也得加


class Friend(Contact):
    def __init__(self, name: str, email: str, phone: str) -> None:
        # super() returns object
        # as if it was actually an instance of the parent class
        # allowing us to call the parent method directly
        super().__init__(name, email)
        self.phone = phone
