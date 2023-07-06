"""
@Description: Combining multiple scopes with ChainMap
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-06 21:30:58
"""

import builtins

builtin_vars = vars(builtins)
key = 'something to search for'

if key in locals():
    value = locals()[key]
elif key in globals():
    value = globals()[key]
elif key in builtin_vars:
    value = builtin_vars[key]
else:
    raise NameError(f'name {key!r} is not defined')

mappings = locals(), globals(), vars(builtins)
for mapping in mappings:
    if key in mapping:
        value = mapping[key]
        break
    else:
        raise NameError(f'name {key!r} is not defined')


from collections import ChainMap
mappings = ChainMap(locals(), globals(), vars(builtins))
mappings[key]
