"""
@Description: Standard API of Mapping Types
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-30 12:37:27
"""
from collections import abc
my_dict = {}
assert isinstance(my_dict, abc.Mapping)
assert isinstance(my_dict, abc.MutableMapping)

tt = (1, 2, (3, 4))
print(hash(tt))
tl = (1, 2, [3, 4])
try:
    print(hash(tl))
except:
    print('[Error] unhashable type')
tf = (1, 2, frozenset([30, 40]))
print(hash(tf))
