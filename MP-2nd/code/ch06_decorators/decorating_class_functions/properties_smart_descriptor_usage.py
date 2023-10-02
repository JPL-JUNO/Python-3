"""
@Title: Properties – Smart descriptor usage
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-26 13:58:25
@Description: 
"""

import functools
from typing import Any


class Sandwich(object):
    def get_eggs(self):
        print("getting eggs")
        return self._eggs

    def set_eggs(self, eggs):
        print("setting eggs to %s" % eggs)
        self._eggs = eggs

    def delete_eggs(self):
        print("deleting eggs")
        del self._eggs
    # as an assignment
    eggs = property(get_eggs, set_eggs, delete_eggs)

    # as a decorator
    @property
    def spam(self):
        print("getting spam")
        return self._spam

    @spam.setter
    def spam(self, spam):
        print("setting spam to %s" % spam)
        self._spam = spam

    @spam.deleter
    def spam(self):
        print("deleting spam")
        del self._spam

    @functools.cached_property
    def bacon(self):
        print("getting bacon")
        return "bacon"


sandwich = Sandwich()
sandwich.eggs = 123
assert sandwich.eggs == 123
del sandwich.eggs

sandwich.bacon
# 只打印一次 getting bacon
# 因为用的是 functools.cached_property
# executes only once per instance
assert sandwich.bacon == "bacon"


class Property(object):
    def __init__(self, fget=None, fset=None, fdel=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel

    def __get__(self, instance, cls):
        if instance is None:
            return self
        elif self.fget:
            return self.fget(instance)

    def __set__(self, instance, value):
        self.fset(instance, value)

    def __del__(self, instance):
        self.fdel(instance)

    def getter(self, fget):
        return Property(fget, self.fset, self.fdel)

    def setter(self, fset):
        return Property(self.fget, fset, self.fdel)

    def deleter(self, fdel):
        return Property(self.fget, self.fset, fdel)


class Sandwich:
    @property
    def eggs(self):
        return self._eggs

    @eggs.setter
    def eggs(self, value): self._eggs = value

    @eggs.deleter
    def eggs(self): del self._eggs


sandwich = Sandwich()
sandwich.eggs = 5
assert sandwich.eggs == 5


class SandwichGenericSolution(object):
    def __init__(self):
        self.registry = {}

    def __getattr__(self, key):
        print("Getting %r" % key)
        return self.registry.get(key, "Undefined")

    def __setattr__(self, key: str, value: Any) -> None:
        if key == "registry":
            object.__setattr__(self, key, value)
        else:
            print("Setting %r to %r" % (key, value))
            self.registry[key] = value

    def __delattr__(self, key: str) -> None:
        print("Deleting %r" % key)
        del self.registry[key]


sandwich = SandwichGenericSolution()
assert sandwich.a == "Undefined"
sandwich.a = 1
assert sandwich.a == 1
del sandwich.a
