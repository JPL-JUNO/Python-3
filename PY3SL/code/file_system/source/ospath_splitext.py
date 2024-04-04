import os.path

PATHS = [
    "filename.txt",
    "filename",
    "/path/to/filename.txt",
    "/",
    "",
    "my-archive.tar.gz",
    "no-extension.",
]
for path in PATHS:
    print(f"{path!r:>21} : {os.path.splitext(path)}")
