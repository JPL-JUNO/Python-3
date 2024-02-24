import os, pathlib, stat

f = pathlib.Path("pathlib_chmod_example.txt")
if f.exists():
    f.unlink()

f.write_text("contents")
existing_permissions = stat.S_IMODE(f.stat().st_mode)
print(f"Before: {existing_permissions:o}")
if not (existing_permissions & os.X_OK):
    print("Adding execute permission")
    new_permissions = existing_permissions | stat.S_IXUSR
else:
    print("Removing execute permission")
    new_permissions = existing_permissions ^ stat.S_IXUSR

f.chmod(new_permissions)
after_permissions = stat.S_IMODE(f.stat().st_mode)
print(f"After: {after_permissions:o}")
