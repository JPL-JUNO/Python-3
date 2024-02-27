import pathlib

p = pathlib.PurePosixPath("./source/pathlib/pathlib_name.py")

print(f"path   : {p}")
print(f"name   : {p.name}")
print(f"suffix : {p.suffix}")
print(f"stem   : {p.stem}")

import os

os.path.splitext("./source/pathlib/pathlib_name.py")
