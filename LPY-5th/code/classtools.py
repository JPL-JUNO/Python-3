"""
@File         : classtools.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-27 21:06:11
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


class AttrDisplay:
    """
    提供可继承的显示重载方法，
    该方法显示实例及其类名
    以及存储在实例本身上的每个属性的键值对
    （但不包括从其类继承的属性）。
    可以混合到任何类中，并且适用于任何实例。
    """

    def gether_attrs(self):
        attrs = []
        for key in sorted(self.__dict__):
            attrs.append(f"{key}={getattr(self, key)}")
        return ", ".join(attrs)

    def __repr__(self) -> str:
        return f"[{self.__class__.__name__}: {self.gether_attrs()}]"


if __name__ == "__main__":

    class TopTest(AttrDisplay):
        count = 0

        def __init__(self) -> None:
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count + 1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X, Y = TopTest(), SubTest()  # Make two instances
    print(X)  # Show all instance attrs
    print(Y)  # Show lowest class name
