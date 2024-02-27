import os.path

FILENAMES = [__file__, os.path.dirname(__file__), "/", "./broken_link"]
for file in FILENAMES:
    print(f"File:{file!r}")
    print(f"Absolute    :", os.path.isabs(file))
    print(f"Is File     :", os.path.isfile(file))
    print(f"Is Dir      :", os.path.isdir(file))
    print(f"Is Link?    :", os.path.islink(file))  # 判断一个路径是否是软链
    print(f"Mountpoint? :", os.path.ismount(file))
    print(f"Exists?     :", os.path.exists(file))
    print(f"Link Exists?:", os.path.lexists(file))
    print()
