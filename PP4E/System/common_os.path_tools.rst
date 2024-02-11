>>> import os
>>> os.sep
'\\'
>>> path_name = r'C:\PP4E\Examples\PP4E\Py_demo.pyw'
>>> os.path.split(path_name)
('C:\\PP4E\\Examples\\PP4E', 'Py_demo.pyw')
>>> path_name.split(os.sep)
['C:', 'PP4E', 'Examples', 'PP4E', 'Py_demo.pyw']
>>> os.sep.join(path_name.split(os.sep))
'C:\\PP4E\\Examples\\PP4E\\Py_demo.pyw'
>>> os.path.join(*path_name.split(os.sep))
'C:PP4E\\Examples\\PP4E\\Py_demo.pyw'
>>>

>>> import os
>>> os.chdir(r"C:\Users")
>>> os.getcwd()
'C:\\Users'
>>> os.path.abspath("")  # empty string means the cwd
'C:\\Users'
>>> os.path.abspath("temp")  # expand to full pathname in cwd
'C:\\Users\\temp'
>>> os.path.abspath(r"PP4E\dev")  # partial paths relative to cwd
'C:\\Users\\PP4E\\dev'
>>> os.path.abspath(".")  # 拓展相对路径句法
'C:\\Users'
>>> os.path.abspath("..")
'C:\\'
>>> os.path.abspath("../examples")
'C:\\examples'
>>> os.path.abspath(r"C:\PP4E\chapters")  # absolute paths unchanged
'C:\\PP4E\\chapters'
>>> os.path.abspath(r"C:\temp\spam.txt")
'C:\\temp\\spam.txt'
>>>