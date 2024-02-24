import pathlib

p = pathlib.Path("../")
for f in p.rglob("*.py"):
    print(f)
