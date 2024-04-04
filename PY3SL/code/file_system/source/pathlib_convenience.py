import pathlib

home = pathlib.Path.home()
print("home:", home)
cwd = pathlib.Path.cwd()
print("cwd:", cwd)

pathlib.Path("/code/ch20/re_anchoring.py")
