"""
@Description: Boolean Indexing to Filter Two-Dimensional Arrays
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-23 17:06:30
"""

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

indices = np.array([[False, False, True],
                    [False, False, False],
                    [True, True, False]])

print(a[indices])

inst = np.array([[232, "@instagram"],
                 [133, "@selenagomez"],
                 [59, "@victoriassecret"],
                 [120, "@cristiano"],
                 [111, "@beyonce"],
                 [76, "@nike"]])

superstars = inst[inst[:, 0].astype(float) > 100, 1]
print(superstars)
