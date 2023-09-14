"""
@Title: 多重继承
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-14 09:34:28
@Description: 
"""

from typing import Protocol

# Protocol tells mypy that
# any class or subclass of Emailable objects must support
# an email attribute, and it must be a string
from commerce_v1 import Contact


class Emailable(Protocol):
    # 协议类通常有一些方法和带有类型提示的类属性（并没有完全赋值）
    email: str


class MailSender(Emailable):
    def send_mail(self, message: str) -> None:
        # print(f"Sending mail to self.email='{self.email}'")
        # 等价于上一条？
        print(f"Sending mail to {self.email=}")
        # some email logic
        # pass


class EmailableContact(Contact, MailSender):
    pass


if __name__ == "__main__":
    e = EmailableContact("John B", "johnb@sloop.net")
    print(Contact.all_contacts)
    e.send_mail("hello")
