>>> from pathlib import Path
>>> 
>>> Path("spam", "bacon", "eggs")
WindowsPath('spam/bacon/eggs')
>>> str(Path("spam", "bacon", "eggs"))
'spam\\bacon\\eggs'
>>> 

>>> my_files = ["accounts.txt", "details.csv", "invite.docx"]
>>> for file in my_files:
...     print(Path(r"C:\Users\Stephen", file))
...
C:\Users\Stephen\accounts.txt
C:\Users\Stephen\details.csv
C:\Users\Stephen\invite.docx
>>>

>>> Path("spam") / "bacon" / "eggs"
WindowsPath('spam/bacon/eggs')
>>> Path("spam") / Path("bacon/eggs")
WindowsPath('spam/bacon/eggs')
>>> Path("spam") / Path("bacon", "eggs")
WindowsPath('spam/bacon/eggs')
>>>

>>> import os
>>>
>>> Path.cwd()
WindowsPath('D:/DS_Works/Python-3/ABSP2E')
>>> os.chdir("C:\\Windows\\System32")
>>> Path.cwd()
WindowsPath('C:/Windows/System32')
>>> os.chdir("C:\\ThisFolderDoesNotExist")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [WinError 2] 系统找不到指定的文件。: 'C:\\ThisFolderDoesNotExist'
>>>

>>> Path.home()
WindowsPath('C:/Users/JPL-JUNO')
>>>

Path.mkdir() 应该是说是能创建文件夹，必须在已有的路径下。

>>> os.makedirs("C:\\delicious\\walnut\\waffles")
>>> Path(r"C:\Users\JPL-JUNO\spam").mkdir()

>>> Path.cwd()
WindowsPath('C:/Windows/System32')
>>> Path.cwd().is_absolute()
True
>>> Path("spam/bacon/eggs").is_absolute()
False
>>>

>>> Path("my/relative/path")
WindowsPath('my/relative/path')
>>> Path.cwd() / Path("my/relative/path")
WindowsPath('C:/Windows/System32/my/relative/path')
>>> Path.home() / Path("my/relative/path")
WindowsPath('C:/Users/JPL-JUNO/my/relative/path')
>>>

>>> os.path.abspath(".")
'C:\\Windows\\System32'
>>> os.path.abspath(".\\Scripts")
'C:\\Windows\\System32\\Scripts'
>>> os.path.isabs(".")
False
>>> os.path.abspath(".")
'C:\\Windows\\System32'
>>> os.path.abspath(".\\Scripts")
'C:\\Windows\\System32\\Scripts'
>>> os.path.isabs(".")
False
>>> os.path.isabs(os.path.abspath("."))
True
>>> os.path.relpath("C:\\Windows", "C:\\")
'Windows'
>>> os.path.relpath("C:\\Windows", "C:\\spam\\eggs")
'..\\..\\Windows'
>>>

>>> p = Path("C:/Users/JPL-JUNO/spam.txt")
>>> p.anchor
'C:\\'
>>> p.parent  # This is a Path object, not a string.
WindowsPath('C:/Users/JPL-JUNO')
>>> p.name
'spam.txt'
>>> p.stem
'spam'
>>> p.suffix
'.txt'
>>> p.drive
'C:'
>>>

>>> p.parents[0]
WindowsPath('C:/Users/JPL-JUNO')
>>> p.parents[0]
WindowsPath('C:/Users/JPL-JUNO')
>>> p.parents[1]
WindowsPath('C:/Users')
>>> p.parents[2]
WindowsPath('C:/')
>>>

>>> os.path.dirname(calc_file_path)
'C:\\Windows\\System32'
>>> os.path.basename(calc_file_path)
'calc.exe'
>>> os.path.split(calc_file_path)
('C:\\Windows\\System32', 'calc.exe')
>>>

>>> calc_file_path.split(os.sep)
['C:', 'Windows', 'System32', 'calc.exe']
>>> "/usr/bin".split('/')
['', 'usr', 'bin']
>>>

>>> os.path.getsize("C:\\Windows\\System32\\calc.exe")
45056
>>> os.listdir("C:\\Windows\\System32")
['%LOCALAPPDATA%', '0409', 
--snip--
]

>>> total_size = 0
>>> for file in os.listdir("C:\\Windows\\System32"):
...     total_size += os.path.getsize(Path("C:\\Windows\\System32") / file)
...
>>> total_size
2453981718
>>>

>>> p = Path("C:/Users/JPL-JUNO/Desktop")
>>> p.glob("*")
<generator object Path.glob at 0x0000028AC4C70370>
>>> list(p.glob("*"))
[WindowsPath('C:/Users/JPL-JUNO/Desktop/!BooksDataBase.xlsx'), 
--snip--
]
>>> list(p.glob("*.txt"))
[]
>>> list(p.glob("project?.docx"))
[]
>>> for text_file_path_obj in p.glob("*.txt"):
...     print(text_file_path_obj)
...
>>>

>>> win_dir = Path("C:/Windows")
>>> not_exist_dir = Path("C:/This/Folder/Does/Not/Exist")
>>> calc_file = Path("C:/Windows/System32/calc.exe")
>>> win_dir.exists()
True
>>> win_dir.is_dir()
True
>>> not_exist_dir.exists()
False
>>> calc_file.is_file()
True
>>> calc_file.is_dir()
False
>>>