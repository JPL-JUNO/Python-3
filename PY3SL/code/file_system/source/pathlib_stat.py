import pathlib, sys, time

if len(sys.argv) == 1:
    filename = __file__
else:
    filename = sys.argv[1]
p = pathlib.Path(filename)
stat_info = p.stat()
print(f"{filename}")
print(f"    Size: {stat_info.st_size}")
print(f"    Permissions: {oct(stat_info.st_mode)}")
print(f"    Owner: {stat_info.st_uid}")
print(f"    Device: {stat_info.st_dev}")
print(f"    Created: {time.ctime(stat_info.st_ctime)}")
print(f"    Last modified: {time.ctime(stat_info.st_mtime)}")
print(f"    Last accessed: {time.ctime(stat_info.st_atime)}")
