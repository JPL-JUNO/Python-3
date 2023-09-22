"""
@Title: 根据字段将记录分组
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 14:35:23
@Description: 
"""

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby
rows.sort(key=itemgetter("date"))

for date, items in groupby(rows, key=itemgetter("date")):
    print(date)
    for i in items:
        print(" ", i)


# 如果只是简单地根据日期将数据分组到一起，放进一个大的数据结构中以允许进行随
# 机访问，那么利用 defaultdict()构建一个一键多值字典可能会更
# 好。
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row["date"]].append(row)

for row in rows_by_date["07/01/2012"]:
    print(row)
# 如果不考虑内存方面的因素，这种方式会比先排序再用 groupby()迭代要来的更快。
