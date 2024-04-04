import pathlib

p = pathlib.Path("example_dir")
print(f"Removing {p}")
p.rmdir()
