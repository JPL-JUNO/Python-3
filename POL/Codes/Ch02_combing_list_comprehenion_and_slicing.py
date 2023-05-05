"""
@Description: Combing List Comprehension and Slicing
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-05 13:48:58
"""

price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
         [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
         [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
         [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]
sample = [line[::2] for line in price]
assert sample == [[9.9, 9.8, 9.5], [9.5, 9.4, 9.2],
                  [8.4, 7.9, 8.0], [7.1, 4.8, 4.7]]
