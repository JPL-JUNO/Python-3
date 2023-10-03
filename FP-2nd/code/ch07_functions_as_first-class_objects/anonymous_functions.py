"""
@Title: Anonymous Functions
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-10-02 21:04:47
@Description: 
"""


def example7_7():
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    print(sorted(fruits, key=lambda word: word[::-1]))
