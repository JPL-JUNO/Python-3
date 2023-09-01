"""
@Title: itertools.compress()
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-01 14:58:35
@Description: 
"""


addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK'
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]
counts = [0, 3, 10, 4, 1, 7, 6, 1]
from itertools import compress
more_5 = [n > 5 for n in counts]
list(compress(addresses, more_5))
