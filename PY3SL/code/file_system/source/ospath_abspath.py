import os
import os.path

os.chdir(os.path.expanduser("~"))
PATHS = [
    ".",
    "..",
    "./one/two/three",
    "../one/two/three",
]
for path in PATHS:
    print(f"{path!r:>21} : {os.path.abspath(path)!r}")
