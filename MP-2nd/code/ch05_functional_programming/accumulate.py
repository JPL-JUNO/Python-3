"""
@Title: reduce with intermediate results
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-23 13:31:58
@Description: The accumulate function is very similar to the reduce function
"""
# The major difference between the reduce and accumulate is that the accumulate function returns the immediate results.

import operator
import itertools

months = [10, 8, 5, 7, 12, 10, 5, 8, 15, 3, 4, 2]
# this function is sometimes called cumsum
list(itertools.accumulate(months, operator.add))
