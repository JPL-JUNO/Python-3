import os.path

PATHS = ["one/two/three", "/one/two/three/", "/", ".", ""]
for path in PATHS:
    print(f"{path!r:>17} : {os.path.basename(path)!r}")
