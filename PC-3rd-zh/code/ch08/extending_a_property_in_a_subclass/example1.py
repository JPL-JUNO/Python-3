"""
@Title: 在子类中扩展属性
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 15:03:52
@Description: 想在子类中扩展某个属性的功能，而这个属性是在父类中定义的。
"""


class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    @property
    def name(self):
        print("Getting name")
        return super().name

    # 如果只想扩展属性中的其中一个方法，可以使用下面的代码实现：
    # @Person.name.getter
    # 当这么做之后，所有之前定义过的属性方法都会被拷贝过来，而 getter 函数则会被替换掉。
    # def name(self):
    #     print("Getting name")
    #     return super().name

    # 如果只想扩展 setter，可以这样：
    # @Person.name.setter
    # def name(self, value):
    #     print("Setting name to", value)
    #     super(SubPerson, SubPerson).name.__set__(self, value)

    @name.setter
    def name(self, value):
        print("Setting name to", value)
        # 为了调用到 setter 之前的
        # 实现，需要把控制流传递到之前定义的 name 属性的__set__()方法中去。但是，唯一
        # 能调用到这个方法的方式就是以类变量而不是实例变量的方式去访问。这正是
        # super(SubPerson, SubPerson)操作所完成的任务。
        super(SubPerson, SubPerson).name.__set__(self, value)

    @name.deleter
    def name(self):
        print("Deleting name")
        super(SubPerson, SubPerson).name.__delete__(self)
