"""
@Title: 拓展内置类 extending built-ins
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-13 21:50:35
@Description: 
"""
from __future__ import annotations


class ContactList(list["Contact"]):
    # 因为引用了还没定义的类，因此需要使用字符串来作为类型引用
    def search(self, name: str) -> list['Contact']:
        match_contacts: list["Contact"] = []
        for contact in self:
            if name in contact.name:
                match_contacts.append(contact)
        return match_contacts


class Contact:
    # 在 v1 中，它就是一个列表，但是这里继承了内置的列表
    # 因此下面使用 append 方法合理的
    # 而且使用 Contact 实例组成的列表
    all_contacts = ContactList()

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r})"
        )


from typing import Optional
# from typing import Union


class LongNameDict(dict[str, int]):
    # dict[str, Union[str, int]]
    # 可以表示 value 是字符或者整数
    """
    作为第二个拓展内置类的例子
    """

    def longest_key(self) -> Optional[str]:
        longest = None
        for key in self:
            # 必须把 longest is None 放在前面
            if longest is None or len(key) > len(longest):
                longest = key
        return longest


if __name__ == '__main__':
    c1 = Contact("John A", "johna@example.net")
    c2 = Contact("John B", "johnb@sloop.net")
    c3 = Contact("Jenna C", "cutty@sark.io")
    print(
        [c.name for c in Contact.all_contacts.search("John")]
    )

    articles_read = LongNameDict()
    articles_read['lucy'] = 42
    articles_read['c_c_phillips'] = 6
    articles_read['steve'] = 7
    print(articles_read.longest_key())
    print(max(articles_read, key=len))
