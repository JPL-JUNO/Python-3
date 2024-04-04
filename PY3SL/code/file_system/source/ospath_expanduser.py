import os.path

for user in ["", "stephen", "nosuchuser"]:
    lookup = "~" + user
    print(f"{lookup!r:>15} : {os.path.expanduser(lookup)!r}")
