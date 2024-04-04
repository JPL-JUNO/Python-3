import pathlib

p = pathlib.Path(__file__)
print(f"{p} is owned by {p.owner()} / {p.group()}")
