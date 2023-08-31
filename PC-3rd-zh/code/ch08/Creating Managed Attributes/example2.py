"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 13:15:38
@Description: 对于已经存在的 get 和 set 方法，同样也可以将它们定义为 property
"""


class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # getter function
    def get_first_name(self):
        return self._first_name

    # setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    # delete function
    def del_first_name(self):
        raise AttributeError("Can't delete attribute")

    # make a property from existing get/set methods
    name = property(get_first_name, set_first_name, del_first_name)
