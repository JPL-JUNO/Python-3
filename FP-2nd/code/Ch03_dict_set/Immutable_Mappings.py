"""
@Description: Immutable Mappings
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-06 13:06:08
"""

from types import MappingProxyType
d = {1: "A"}
d_proxy = MappingProxyType(d)
print(d_proxy)

# d_proxy可以访问d中的项
assert d_proxy[1] == "A"
try:
    # 不能通过d_proxy更改原映射
    d_proxy[2] = 'x'
except TypeError as e:
    print(e)

# d_proxy是动态的，因此可以反应d的变化
d[2] = 'B'
print(d_proxy)
assert d_proxy[2] == 'B'
