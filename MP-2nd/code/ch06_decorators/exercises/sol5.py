"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-28 15:33:51
@Description: Create a version of functools.cached_property that can be recalculated as needed.
"""

from datetime import datetime


class _NotFound:
    pass


class CachedProperty:
    def __init__(self, func):
        self.func = func

    def clear(self):
        self.cache.pop(self.attrname, None)

    def __set_name__(self, owner, name):
        if not hasattr(owner, "_cache"):
            owner._cache = dict()
            setattr(owner, f"clear_{name}", self.clear)
        self.cache = owner._cache
        self.attrname = name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self

        key = self.attrname
        if key not in self.cache:
            self.cache[key] = self.func(instance)

        return self.cache[key]


class SomeClass:

    @CachedProperty
    def current_time(self):
        return datetime.now()


def main():
    some_class = SomeClass()
    a = some_class.current_time
    b = some_class.current_time
    assert a == b
    # Clear the cache. Even though your editor might complain, this method
    # exists. Can you think of a better API to make the cache clearable?
    # 这里似乎有点问题❌
    some_class.clear_current_time()
    c = some_class.current_time
    assert a == c  # ✅
    # assert a != c  # ❌


if __name__ == '__main__':
    main()
