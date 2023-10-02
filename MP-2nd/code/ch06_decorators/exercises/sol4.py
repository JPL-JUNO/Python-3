"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-28 15:26:13
@Description: Modify the memoization function to have a cache per function instead of a global one.
"""
import functools


def memoize(function):
    function.cache = dict()

    def safe_hash(args):
        try:
            return hash(args)
        except TypeError:
            return repr(args)

    @functools.wraps(function)
    def _memoize(*args):
        key = safe_hash(args)
        if key not in function.cache:
            function.cache[key] = function(*args)
        return function.cache[key]
    return _memoize


@memoize
def printer(*args):
    print(args)


def main():
    printer('a', 'b', 'c')
    printer(dict(a=1, b=2, c=3))


if __name__ == '__main__':
    main()
