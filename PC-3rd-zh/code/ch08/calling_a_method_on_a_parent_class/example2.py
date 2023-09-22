"""
@Title: 调用父类中的方法
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 14:23:14
@Description: super()函数的一种常见用途是调用父类的__init__()方法，确保父类被正确地初始化了
"""


class A:
    def __init__(self):
        self.x = 0


class B(A):
    def __init__(self):
        super().__init__()
        self.y = 1
