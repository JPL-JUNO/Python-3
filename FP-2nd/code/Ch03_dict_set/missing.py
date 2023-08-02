"""
@Description: __missing__方法
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-04 12:46:58
"""

from collections import UserDict
from collections import abc


def _upper(x):
    try:
        return x.upper()
    except AttributeError:
        return x


class DictSub(dict):
    def __missing__(self, key):
        return self[_upper(key)]


class UserDictSub(UserDict):
    def __missing__(self, key):
        return self[_upper(key)]


class SimpleMappingSub(abc.Mapping):
    def __init__(self, *args, **kwargs) -> None:
        self._data = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self._data[key]

    def __len__(self):
        return len(self._data)

    def __iter__(self):
        return iter(self._data)

    def __missing__(self, key):
        return self[_upper(key)]


class MappingMissingSub(SimpleMappingSub):
    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            return self[_upper(key)]


class DictLikeMappingSub(SimpleMappingSub):
    def __getitem__(self, key):
        try:
            return self._data[key]
        except KeyError:
            return self[_upper(key)]

    def get(self, key, default=None):
        return self._data.get(key, default)

    def __contains__(self, key):
        return key in self._data


if __name__ == '__main__':
    # ✅表示调用了__missing__

    # Subclass of ``dict``
    d = DictSub(A='letter A')
    print(d['a'])  # ✅
    print(d.get('a', 'empty'))
    print('a' in d)
    print('--------------------------------------------------------')
    ud = UserDictSub(A='letter A')
    # UserDict子类，d[k]和d.get(k)在查找键时可能会调用__missing__方法
    print(ud['a'])  # ✅
    print(ud.get('a', 'empty'))  # ✅
    print('a' in ud)
    print('--------------------------------------------------------')
    sms = SimpleMappingSub(A='letter A')
    # abc.Mapping子类，已简单方式实现__getitem__，永不触发__missing__
    try:
        sms['a']
    except KeyError:
        print('KeyError')
    print(sms.get('a', 'empty'))
    print('a' in sms)

    print('--------------------------------------------------------')
    # 让__getitem__调用__missing__方法，d[k], d.get(k), k in d都将触发__missing__
    mms = MappingMissingSub(A='letter A')
    print(mms['a'])  # ✅
    print(mms.get('a', 'empty'))
    assert 'a' in mms

    print('--------------------------------------------------------')
    dms = DictLikeMappingSub(A='letter A')
    print(dms['a'])  # ✅
    print(dms.get('a', 'empty'))
    assert 'a' not in dms
