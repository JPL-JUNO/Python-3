import subprocess

subprocess.call("python helloshell.py")

pipe = subprocess.Popen("python helloshell.py", stdout=subprocess.PIPE)
pipe.communicate()
pipe.returncode

pipe = subprocess.Popen("python helloshell.py", stdout=subprocess.PIPE)
pipe.stdout.read()
pipe.wait()

from subprocess import Popen, PIPE

Popen("python helloshell.py", stdout=PIPE).communicate()[0]

import os

os.popen("python helloshell.py").read()
