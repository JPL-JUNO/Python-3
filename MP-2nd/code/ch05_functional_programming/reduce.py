"""
@Title: reduce
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-23 11:40:23
@Description: Combining pairs into a single result
"""
# The reduce function implements a mathematical technique called folding.
# It applies a pair of the
# previous result and the next item in the given list to the function that is passed.

import operator
import functools
# 这里就体现了 operator 的用处，即操作符的函数式
assert functools.reduce(operator.mul, range(1, 5)) == 24

from operator import mul
assert mul(mul(mul(1, 2), 3), 4) == 24


def reduce(function, iterable):
    print(f"Iterable={iterable}")
    # split an iterable between the first item and the remaining ones.
    result, *iterable = iterable
    for item in iterable:
        old_result = result
        result = function(result, item)
        print(f"{old_result} * {item} = {result}")
    return result


iterable = list(range(1, 5))
print(iterable)

print(reduce(operator.mul, iterable))

print("----- Processing trees -----")
# Trees are a case where the reduce function really shines.
import json
import functools
import collections


def tree():
    return collections.defaultdict(tree)


taxonomy = tree()
reptilia = taxonomy['Chordata']['Vertebrata']['Reptilia']
reptilia['Squamata']['Serpentes']["Pythonidae"] = [
    "Liasis", "Morelia", "Python"]

print(json.dumps(taxonomy, indent=4))


def lookup(tree, path):
    # Split the path for easier access
    path = path.split('.')
    return functools.reduce(operator.getitem, path, tree)


path = "Chordata.Vertebrata.Reptilia.Squamata.Serpentes"
print(dict(lookup(taxonomy, path)))


path = "Chordata.Vertebrata.Reptilia.Squamata"
print(lookup(taxonomy, path).keys())

print("----- Reducing in the other direction -----")
initializer = 0


def function(x, y):
    pass


fold_left = functools.reduce(
    lambda x, y: function(x, y),
    iterable,
    initializer,
)

fold_right = functools.reduce(
    lambda x, y: function(x, y),
    reversed(iterable),
    initializer
)
