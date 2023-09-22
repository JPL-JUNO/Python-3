"""
@Title: 简单的测试程序
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 16:15:24
@Description: 
"""

from area import rect_area
height = 3
width = 4
correct_answer = 12
answer = rect_area(height, width)
if answer == correct_answer:
    print("Test passed")
else:
    print("Test failed")
