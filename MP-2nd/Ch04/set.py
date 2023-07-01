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


current_users = set(('a', 'b', 'd'))
new_users = set(('d', 'c', 'd', 'e'))
to_insert = new_users - current_users
to_delete = current_users - new_users
unchanged = current_users & new_users

