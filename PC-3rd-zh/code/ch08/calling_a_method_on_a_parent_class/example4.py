"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 14:29:49
@Description: 偶尔我们会看到一些代码直接调用父类中的方法
"""


class Base:
    def __init__(self):
        print("Base.__init__")


class A(Base):
    def __init__(self):
        Base.__init__(self)
        print("A.__init__")


class B(Base):
    def __init__(self):
        Base.__init__(self)
        print("B.__init__")


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("C.__init__")

# 尽管对于大部分代码来说这么做都“行得通”，但是在涉及多重继承的代码里，就会导
# 致出现奇怪的麻烦。
