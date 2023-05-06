"""
@Description: Conditional Array Search, Filtering, and Broadcasting to Detect Outliers
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-06 15:21:45
"""

import numpy as np

X = np.array([[1, 0, 0],
              [0, 2, 2],
              [3, 0, 0]])
print(np.nonzero(X))
