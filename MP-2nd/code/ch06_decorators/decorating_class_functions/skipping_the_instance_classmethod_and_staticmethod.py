"""
@Title: Skipping the instance – classmethod and staticmethod
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-26 12:49:33
@Description: 
"""
import pprint


class Spam(object):
    def some_instance_method(self, *args, **kwargs):
        pprint.pprint(locals(), width=60)

    @classmethod
    def some_class_method(cls, *args, **kwargs):
        pprint.pprint(locals(), width=60)

    @staticmethod
    def some_static_method(*args, **kwargs):
        pprint.pprint(locals(), width=60)


# Create an instance so we can compare the difference between
# executions with and without instances easily
spam = Spam()
# with an instance (not the lowercase spam)
spam.some_instance_method(1, 2, a=3, b=4)

# without an instance (note the capitalized Spam)
try:
    Spam.some_instance_method()
except TypeError as err:
    print(err)
# But what if we add parameters?
# Be very careful with these!
# Our first argument is now used as an argument, this can give
# very strange and unexpected errors
Spam.some_instance_method(1, 2, a=3, b=4)
# 并不会检查第一个参数是不是 Spam 的实例
# Spam.some_instance_method(spam) is identical to
# spam.some_instance_method()

# Classmethod are expectedly identical
spam.some_class_method(1, 2, a=3, b=4)

Spam.some_class_method()
Spam.some_class_method(1, 2, a=3, b=4)
# the main difference here is that instead of self we now have cls
# which contains the class (Spam) instead of the instance (spam)

# the staticmethod behaves identically to a regular
# function outside of a class
spam.some_static_method(1, 2, a=3, b=4)
Spam.some_static_method()
Spam.some_static_method(1, 2, a=3, b=4)


class Spam:
    def __init__(self, spam=1):
        self.spam = spam

    def __get__(self, instance, cls):
        return self.spam + instance.eggs

    def __set__(self, instance, value):
        instance.eggs = value - self.spam


class Sandwich:
    spam = Spam(5)

    def __init__(self, eggs) -> None:
        self.eggs = eggs


sandwich = Sandwich(1)
assert sandwich.eggs == 1
# whenever we set or get value from sandwich.spam,
# it actually calls __get__ or __set__ on Spam
# which has access not only to its own variables,
# but also the calling class
assert sandwich.spam == 6
sandwich.eggs = 10
assert sandwich.spam == 15

import functools


class ClassMethod(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, cls):
        @functools.wraps(self.method)
        def method(*args, **kwargs):
            return self.method(cls, *args, **kwargs)
        return method


class StaticMethod(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, instance, cls):
        return self.method


class Sandwich:
    spam = "class"

    def __init__(self, spam):
        self.spam = spam

    @ClassMethod
    def some_class_method(cls, arg):
        return cls.spam, arg
    # some_class_method = ClassMethod(some_class_method(cls, arg))

    @StaticMethod
    def some_static_method(arg):
        return Sandwich.spam, arg


sandwich = Sandwich("instance")
assert sandwich.spam == "instance"
assert sandwich.some_class_method("argument") == ('class', "argument")
assert sandwich.some_static_method("argument") == ("class", "argument")
