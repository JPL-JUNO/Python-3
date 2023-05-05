"""
@Description: Analyzing Cardiac Health Data with List Concatenation
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-05 21:29:52
"""

import matplotlib.pyplot as plt

cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]
expected_cycle = cardiac_cycle[1:-2] * 10
plt.plot(expected_cycle)
plt.show()
