"""
@Description: Conditional Array Search, Filtering, and Broadcasting to Detect Outliers
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-23 16:51:20
"""

import numpy as np

X = np.array([[1, 0, 0],
              [0, 2, 2],
              [3, 0, 0]])
print(np.nonzero(X))

print(X == 2)

X = np.array(
    [[42, 40, 41, 43, 44, 43],  # Hong Kong
     [30, 31, 29, 29, 29, 30],  # New York
     [8, 13, 31, 11, 11, 9],  # Berlin
     [11, 11, 12, 13, 11, 12]])  # Montreal

cities = np.array(['Hong Kong', 'New York', 'Berlin', 'Montreal'])
polluted = set(cities[np.nonzero(X > np.average(X))[0]])
print(polluted)
