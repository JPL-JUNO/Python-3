import pathlib, time

p = pathlib.Path("touched")
if p.exists():
    print("Already exists")
else:
    print("creating new")
p.touch()
start = p.stat()
time.sleep(1)
p.touch()
end = p.stat()
print("Start:", time.ctime(start.st_mtime))
print("End  :", time.ctime(end.st_mtime))
