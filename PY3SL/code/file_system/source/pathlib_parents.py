import pathlib

p = pathlib.PurePosixPath("/usr/local/lib")

print(f"parent: {p.parent}")
print("Hierarchy:")
for up in p.parents:
    print(up)
