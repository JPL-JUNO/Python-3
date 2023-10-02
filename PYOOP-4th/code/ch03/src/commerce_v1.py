"""
@Title: 基础继承 Basic Inheritance
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-13 21:10:40
@Description: 
"""
from typing import List


class Contact:
    """
    负责维护一个类变量中所有联系人的列表
    >>> c_1 = Contact("Dusty", "dusty@example.com")
    >>> c_2 = Contact("Steve", "steve@itmaybeahack.com")
    >>> Contact.all_contacts
    [Contact('Dusty', 'dusty@example.com'), 
     Contact('Steve','steve@itmaybeahack.com')]
    """
    # 类变量，由所有的实例共享
    # 这里是用来保存所有的实例
    all_contacts: List["Contact"] = []

    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"{self.name!r}, {self.email!r})"
        )


class Supplier(Contact):
    # 数据也会被收集到 Contact.all_contacts
    def order(self, order: "Order") -> None:
        print("If this were a real system we would send "
              f"'{order}' order to '{self.name}'")


if __name__ == "__main__":
    c_1 = Contact("Dusty", "dusty@example.com")
    c_2 = Contact("Steve", "steve@itmaybeahack.com")
    print(Contact.all_contacts)

    c = Contact("Some Body", "somebody@example.com")
    s = Supplier("Sup Plier", "supplier@example.com")
    print(c.name, c.email, s.name, s.email)
    from pprint import pprint
    pprint(c.all_contacts)

    try:
        # 没有方法
        c.order
    except AttributeError as e:
        print(e)

    s.order("I need pliers")
