import os.path
import os

os.environ["MYVAR"] = "VALUE"
os.path.expandvars("/path/to/$MYVAR")
