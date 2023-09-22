"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 17:03:33
@Description: 利用关键字参数来给类添加额外的属性，这些额外的属性是没有定义在_fields 中的。
"""


class Structure:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        # 🚩
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError("Duplicate values for {}".format(",".join(kwargs)))


if __name__ == "__main__":
    class Stock(Structure):
        _fields = ["name", "shares", "price"]
    s1 = Stock("ACME", 50, 91.1)
    s2 = Stock("ACME", 50, 91.1, date="2023-08-31")
