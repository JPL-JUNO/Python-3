"""
@Description: using slice assignment to correct corrupted lists
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-05-05 20:58:52
"""

visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted',
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

visitors[1::2] = visitors[::2]
print(visitors)
