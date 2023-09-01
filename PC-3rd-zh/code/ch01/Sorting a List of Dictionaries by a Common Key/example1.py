"""
@Title: 通过公共键对字典列表排序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 14:14:18
@Description: 
"""

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter("fname"))
rows_by_uid = sorted(rows, key=itemgetter("uid"))

print(rows_by_uid)
print(rows_by_fname)

rows_by_lfname = sorted(rows, key=itemgetter("lname", "fname"))
print(rows_by_lfname)

rows_by_fname = sorted(rows, key=lambda r: r["fname"])
rows_by_uid = sorted(rows, key=lambda r: r["uid"])
# 但是用 itemgetter()通常会运行得更快一些。

min(rows, key=itemgetter("uid"))
max(rows, key=itemgetter("fname"))
