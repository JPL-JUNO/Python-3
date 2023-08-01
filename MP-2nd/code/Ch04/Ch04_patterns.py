"""
@Description: Global instances using Borg or Singleton patterns
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-22 23:53:23
"""

# Borg 设计模式是 Singleton 模式的变体，它允许类的多个实例共享相同的状态。
# 在 Borg 模式中，类的所有实例都具有共享状态，这意味着如果一个实例修改状态，所有其他实例都会反映该更改。

# 当您想要创建共享相同状态的类的多个实例时，Borg 模式会很有用，
# 而不是强制执行严格的单例模式（在应用程序的整个生命周期中只存在一个实例）。
# 它提供了一种实现某种级别的共享状态的方法，同时仍然允许在必要时创建多个实例。


class Borg:
    # 它充当类的所有示例的共享状态
    _shared_state = {}

    def __init__(self):
        # 在 Python 中，__dict__ 属性是报错对象属性的字典
        # 将 __dict__ 类的每个实例的属性设置到共享 _state 字典中
        self.__dict__ = self._shared_state


class SubBorg(Borg):
    pass


a = Borg()
b = Borg()
c = Borg()
a.a_property = 123
assert b.a_property == 123
assert c.a_property == 123


# Singleton 模式确保一个类只有一个实例，并提供对该实例的全局访问点。
# 任何后续创建该类的新实例的尝试都将返回最初创建的相同实例。

class Singleton:
    # 在对象创建期间在该方法之前被调用 __init__
    def __new__(cls):
        if not hasattr(cls, '_instance'):
            # If no instance exists,
            # this line creates a new instance of the class using the super() function
            # and assigns it to the _instance attribute of the class.
            cls._instance = super(Singleton, cls).__new__(cls)

        return cls._instance


class SubSingleton(Singleton):
    pass


a = Singleton()
b = Singleton()
c = SubSingleton()
a.a_property = 123
assert b.a_property == 123
assert c.a_property == 123
