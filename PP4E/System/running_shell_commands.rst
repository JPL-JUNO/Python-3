>>> import os
>>> os.system('dir /B')
.vscode
code.rst
common_os.path_tools.py
common_os.path_tools.rst
exception_details.py
exception_details.rst
loaded_modules_table.py
loaded_modules_table.rst
module_search_path.py
more.py
more.rst
notes.py
platforms_and_versions.py
portability_constants.py
portability_constants.rst
rename.py
running_shell_commands.rst
string_method_basics.py
tools_in_the_os_module.rst
__pycache__
0
>>> os.system('type rename.py')
import os

for file in os.listdir():
    # print(__file__)
    # print(file)
    os.rename(file, file.replace(" ", "_").lower())
0
>>> os.system('type rename1.py')
系统找不到指定的文件。
1
>>> open('rename.py').read()
'import os\n\nfor file in os.listdir():\n    # print(__file__)\n    # print(file)\n    os.rename(file, file.replace(" ", "_").lower())\n'
>>> text = os.popen('type rename.py').read()
>>> text
'import os\n\nfor file in os.listdir():\n    # print(__file__)\n    # print(file)\n    os.rename(file, file.replace(" ", "_").lower())\n'
>>>

>>> listing = os.popen('dir /B').readlines()
>>> listing
['.vscode\n', 'code.rst\n', 'common_os.path_tools.py\n', 'common_os.path_tools.rst\n', 
'exception_details.py\n', 'exception_details.rst\n', 'loaded_modules_table.py\n', 
'loaded_modules_table.rst\n', 'module_search_path.py\n', 'more.py\n', 'more.rst\n', 
'notes.py\n', 'platforms_and_versions.py\n', 'portability_constants.py\n', 'portability_constants.rst\n', 
'rename.py\n', 'running_shell_commands.rst\n', 'string_method_basics.py\n', 'tools_in_the_os_module.rst\n', 
'__pycache__\n']

