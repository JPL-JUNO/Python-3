"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-20 12:43:26
@Description: 
"""

from itertools import cycle
for i in zip(range(7), cycle(['a', 'b', 'c'])):
    print(i)
