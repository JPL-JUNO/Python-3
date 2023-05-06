"""
@Description: Basic Two-Dimensional Array Arithmetic
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-06 13:45:39
"""
import numpy as np

alice = [99, 101, 103]
bob = [110, 108, 105]
tim = [90, 88, 85]
salaries = np.array([alice, bob, tim])
taxation = np.array([[0.2, 0.25, 0.22],
                     [0.4, 0.5, 0.5],
                     [0.1, 0.2, 0.1]])
max_income = np.max(salaries - salaries*taxation)
assert max_income == 81.0
