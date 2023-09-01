"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 14:34:03
@Description: 
"""


class Base:
    def __init__(self):
        print("Base.__init__")


class A(Base):
    def __init__(self):
        super().__init__()
        print("A.__init__")


class B(Base):
    def __init__(self):
        super().__init__()
        print("B.__init__")


class C(A, B):
    def __init__(self):
        super().__init__()  # Only one call to super() here
        print("C.__init__")
