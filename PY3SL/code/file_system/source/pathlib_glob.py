import pathlib

p = pathlib.Path(".")
for f in p.glob("*.rst"):
    print(f)
