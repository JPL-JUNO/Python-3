"""
@File         : 1_4_built-in_scope.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-28 13:07:56
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import builtins

dir(builtins)

zip

builtins.zip

assert zip is builtins.zip

len(dir(builtins)), len([x for x in dir(builtins) if not x.startswith("__")])

# __builtins__ 并不是内置的（注意这里有 s），只是交互式命令行的一个变量
# 在 import builtins 后，有
assert builtins is __builtins__
