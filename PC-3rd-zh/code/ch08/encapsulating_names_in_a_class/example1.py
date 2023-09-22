"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 11:48:31
@Description: 
"""


class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        """
        A public method
        """
        pass

    def _internal_method(self):
        pass


class B:
    """私有属性会被分别重命名为_B__private 和_B__private_method"""

    def __init__(self):
        self.__private = 0

    def __private_method(self):
        pass

    def public_method(self):
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1  # Does not override B.__private
    # 这里 ，私有名称 __private 和__private_method 会被重命名为
    # _C__private 和 _C__private_method，这和基类 B 中的重整名称不同。

    def __private_method(self):
        # Does not override B.__private_method()
        pass
