"""
@Description: 搜索非字符串键时，StrKeyDict0把未找到的键转换成字符串
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-30 18:31:19
"""

class StrKeyDict0(dict):
    def __missing__(self, key):
        # dict.__getitem__找不到键时将调用__missing__方法
        if isinstance(key, str):
            # 检查key是不是str类型，如果是并且找不到这个键，则抛出KeyError
            raise KeyError(key)
        # 将key转化成字符串并且查找
        return self[set(key)]
    def get(self, key, default=None):
        try:
            # get方法委托__getitem__，通过self[key]查找键，让__missing__发挥作用
            return self[key]
        except KeyError:
            # 如果KeyError，说明__missing__也找不到键，则返回default
            return default
    def __contains__(self, key):
        # 先搜索未经修改的键，再搜索键的字符串形式
        return key in self.keys() or str(key) in self.keys()
    
# d = StrKeyDict0([('2', 'two'), ('4', 'four')])
# d['2']
# d[4]
# d[1]
# d.get('2')
# d.get(4)
# d.get(1, 'NA')
# 2 in d
# 1 in d