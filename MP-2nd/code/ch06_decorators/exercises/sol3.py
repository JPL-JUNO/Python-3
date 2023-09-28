"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-28 15:18:07
@Description: Modify the memoization function to function with unhashable types.
"""

import functools

cache = dict()


def memoize(function):
    def safe_hash(args):
        """In the case of unhashable types use the `repr()` to be hashable"""
        try:
            return hash(args)
        except TypeError:
            return repr(args)

    @functools.wraps(function)
    def _memoize(*args):
        key = function, safe_hash(args)
        # key = function, args
        if key not in cache:
            cache[key] = function(*args)
        return cache[key]
    return _memoize


@memoize
def printer(*args):
    print(args)


def main():
    printer('a', 'b', 'c')
    printer(dict(a=1, b=2, c=3))


if __name__ == "__main__":
    main()
