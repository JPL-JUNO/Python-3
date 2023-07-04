"""
@Description: collections.Counter
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-04 13:29:02
"""
import collections
ct = collections.Counter('abracadabra')
print(ct)
ct.update('aaaaazzzz')
print(ct)
print(ct.most_common(3))
