import os.path

PATHS = [
    "one//two//three",
    "one/./two/./three",
    "one/../alt/two/three",
]
for path in PATHS:
    print(f"{path!r:>22} : {os.path.normpath(path)}")
