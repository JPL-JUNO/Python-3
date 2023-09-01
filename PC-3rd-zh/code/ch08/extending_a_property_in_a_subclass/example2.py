"""
@Title: 扩展描述符
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 15:18:45
@Description: 
"""


# A descriptor
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        instance.__dict__[self.name] = value


class Person:
    name = String("name")

    def __init__(self, name):
        self.name = name


class SubPerson(Person):
    @property
    def name(self):
        print("Getting name")
        return super().name

    @name.setter
    def name(self, value):
        print("Setting name to", value)
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print("Deleting name")
        super(SubPerson, SubPerson).name.__delete__(self)
