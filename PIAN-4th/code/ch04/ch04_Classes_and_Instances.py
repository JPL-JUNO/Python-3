"""
@Description: Classes and Instances
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-25 09:17:21
"""


class C1:
    # You usually specify an attribute of a class object
    # by binding a value to an identifier within the class body.
    x = 23


print(C1.x)


class C2:
    pass


# You can also bind or unbind class attributes outside the class body.
C2.x = 23
print(C2.x)

# The class statement implicitly sets some class attributes.
# The attribute __name__ is the Classname identifier string used in the class statement.
# The attribute __bases__ is the tuple of class objects given (or implied) as the base classes in
# the class statement.
print(C1.__name__, C1.__base__)

# A class also has an attribute called __dict__, which is the read-only mapping
# that the class uses to hold other attributes (also known, informally, as the class’s
# namespace).
print(C1.__dict__)


class C3:
    # In statements directly in a class’s body,
    # references to class attributes must use a
    # simple name, not a fully qualified name.
    x = 23
    y = x + 22


class C4:
    x = 23
    # However, in statements within methods defined in a class body, references to class
    # attributes must use a fully qualified name, not a simple name.

    def a_method(self):
        print(C4.x)


c = C4()
c.a_method()


class C5:
    # a method defined in a class body has a mandatory first parameter, conventionally
    # always named self, that refers to the instance on which you call the method. The
    # self parameter plays a special role in method calls
    def hello(self):
        print('Hello')


# Descriptors
print('===== Descriptors ======')


class Const:  # class with an overriding descriptor, see later
    def __init__(self, value):
        self.__dict__['value'] = value

    def __set__(self, *_):
        # silently ignore any attempt at deleting
        # (a better design choice might be to raise AttributeError)
        pass

    def __get__(self, *_):
        # always return the constant value
        return self.__dict__['value']

    def __delete__(self, *_):
        # silently ignore any attempt at deleting
        # (a better design choice might be to raise AttributeError)
        pass


class X:
    c = Const(23)


x = X()
print(x.c)
x.c = 42
assert x.c == 23
del x.c
assert x.c == 23

assert isinstance('c', type(None) | str)
print(type(None))
