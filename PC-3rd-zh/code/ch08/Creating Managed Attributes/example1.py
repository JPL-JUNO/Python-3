"""
@Title: 创建可管理的属性
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 13:02:50
@Description: 在对实例属性的获取和设定上，我们希望增加一些额外的处理过程（比如类型检查或者验证）。
"""


class Person:
    def __init__(self, first_name):
        # self.first_name 实际上会调用到 setter 方法，
        self.first_name = first_name

    # getter function
    @property
    def first_name(self):
        return self._first_name

    # 需要重点强调的是，除非 first_name 已经通
    # 过@property 的方式定义为了 property 属性，否则是不能定义@first_name.setter 和
    # @first_name.deleter 装饰器的。

    # setter function
    @first_name.setter
    def first_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    # Deleter function(optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")
