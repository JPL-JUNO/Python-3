"""
@Description: Broadcasting, Slice Assignment, and Reshaping to Clean Every i-th Array Element
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-23 17:19:54
"""
import numpy as np
tmp = np.array([1, 2, 3, 4, 3, 4, 4,
                5, 3, 3, 4, 3, 4, 6,
                6, 5, 5, 5, 4, 5, 5])
tmp[6::7] = np.average(tmp.reshape((-1, 7)), axis=1)
print(tmp)
