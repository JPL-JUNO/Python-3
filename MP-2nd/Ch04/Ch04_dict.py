"""
@Description: Dict union operators
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-07-23 23:09:57
"""

# old solution
a = dict(x=1, y=2)
b = dict(y=1, z=2)
c = a.copy()
print(c)
c.update(b)
print(a)
print(b)
print(c)

import sys
# from distutils.version import LooseVersion
import platform
from packaging import version

python_ver = platform.python_version()
# deprecated warning
# if LooseVersion(sys.version) < LooseVersion('3.8'):
if version.parse(python_ver) < version.parse('3.8'):
    print(
        f'[FAIL] We recommend Python 3.8 or later but found version {sys.version}')
else:
    print(f'[OK] Your Python Version is {sys.version}')

a = dict(x=1, y=2)
b = dict(y=1, z=2)
c = a | b
# c['x'] = 999
# print(a)
print(c)

# This is a feature that can be very convenient when specifying arguments to a function,
# especially if you want to automatically fill in keyword arguments with default arguments:
