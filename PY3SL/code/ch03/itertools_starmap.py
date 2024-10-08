"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 10:59:44
@Description: 
"""

from itertools import starmap

values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
for i in starmap(lambda x, y: (x, y, x * y), values):
    print("{} * {} = {}".format(*i))

# for (x, y) in values:
#     print(x, y, x * y)
