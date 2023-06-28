"""
@Description: set – Like a dict without values
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-06-28 10:41:13
"""

def print_set(expression, set_):
    """Print set as a string sorted by letters"""
    print(expression, ''.join(sorted(set_)))
    
spam = set('spam')
print_set('spam:', spam)

eggs = set('eggs')
print_set('eggs:', eggs)