"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 16:55:09
@Description: 对关键字参数做映射，这样它们就只对应于定义在_fields 中的属性名。
"""


class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name in self._fields[len(args):]:
            setattr(self, name, kwargs.pop(name))

        # Check for any remaining unknown arguments
        if kwargs:
            raise TypeError("Invalid argument(s): {}".format(','.join(kwargs)))


if __name__ == "__main__":
    class Stock(Structure):
        _fields = ["name", "shares", "price"]
    s1 = Stock("ACME", 50, 91.1)
    s2 = Stock("ACME", 50, price=91.1)
    s3 = Stock("ACME", shares=50, price=91.1)
