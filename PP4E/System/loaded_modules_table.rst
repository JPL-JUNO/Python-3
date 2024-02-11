>>> import sys
>>> sys.modules
{'sys': <module 'sys' (built-in)>, 'builtins': ...more deleted...
>>> list(sys.modules.keys())
['sys', 'builtins', '_frozen_importlib', ...more deleted...
>>> sys
<module 'sys' (built-in)>
>>> sys.modules['sys']
<module 'sys' (built-in)>