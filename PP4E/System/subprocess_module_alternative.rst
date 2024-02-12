>>> import subprocess
>>> subprocess.call('python helloshell.py') # 类似于 os.system()
The Meaning of Life
0
>>> subprocess.call('cmd /C "type helloshell.py"') # 内建 shell 命令
# a Python program
print("The Meaning of Life")
0
>>> subprocess.call('type helloshell.py', shell=True)
# a Python program
print("The Meaning of Life")
0
>>>

>>> pipe = subprocess.Popen("python helloshell.py", stdout=subprocess.PIPE)
>>> pipe.communicate()
(b'The Meaning of Life\r\n', None)
>>> pipe.returncode
0
>>>

>>> pipe = subprocess.Popen("python helloshell.py", stdout=subprocess.PIPE)
>>> pipe.stdout.read()
b'The Meaning of Life\r\n'
>>> pipe.wait()
0
>>>

实际上， os.popen() 和 subprocess.Popen() 之间存在直接的映射关系：

>>> from subprocess import Popen, PIPE
>>> Popen("python helloshell.py", stdout=PIPE).communicate()[0]
b'The Meaning of Life\r\n'
>>>
>>> import os
>>> os.popen("python helloshell.py").read()
'The Meaning of Life\n'
>>>