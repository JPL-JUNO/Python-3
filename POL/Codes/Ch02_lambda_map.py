"""
@Description: Using lambda and Map Functions
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-04 22:23:38
"""

txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

mask = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
# print(list(mask))

mask_list_comprehension = [
    (True, s) if 'anonymous' in s else (False, s) for s in txt]

assert list(mask) == mask_list_comprehension
