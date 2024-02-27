"""
@File         : 2 3 Other Iteration Contexts.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-01-24 19:59:32
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

for line in open("./script2.py"):
    print(line.upper(), end="")

uppers = [line.upper() for line in open("./script2.py")]
print(uppers)

map(str.upper, open("./script2.py"))

list(map(str.upper, open("./script2.py")))

sorted(open("./script2.py"))
list(zip(open("./script2.py"), open("./script2.py")))
list(enumerate("./script2.py"))
# non-empty == True
list(filter(bool, open("./script2.py")))

list(open("./script2.py"))
tuple(open("./script2.py"))
"&&".join(open("./script2.py"))

a, b, c, d, e = open("./script2.py")
print(a, d)

a, *d = open("./script2.py")
print(a, d)

"y = 2\n" in open("./script2.py")
assert "x = 2\n" in open("./script2.py")

L = [11, 22, 33, 44]
L[1:3] = open("./script2.py")
print(L)

L = [11]
L.extend(open("./script2.py"))
print(L)

L = [11]
L.append(open("./script2.py"))
print(L)
list(L[1])

set(open("./script2.py"))

{line for line in open("./script2.py")}

{idx: line for idx, line in enumerate(open("./script2.py"))}

{line for line in open("./script2.py") if line.startswith("p")}

{idx: line for (idx, line) in enumerate(open("./script2.py")) if line.startswith("p")}

# 生成器表达式
list(line.upper() for line in open("./script2.py"))

sum([3, 2, 4, 1, 5, 0])
any(["spam", "", "ni"])
all(["spam", "", "ni"])

max([3, 2, 5, 1, 4])
min([3, 2, 5, 1, 4])

max(open("./script2.py"))
min(open("./script2.py"))


def f(a, b, c, d, e):
    print(a, b, c, d, e, sep="&")


# 这种调用中的参数解包语法能够接受可迭代对象
f(1, 2, 3, 4, 5)
f(*[1, 2, 3, 4, 5])
f(*open("./script2.py"))


X = (1, 2, 5)
Y = (3, 4, 9)
list(zip(X, Y))

# 这种调用中的参数解包语法能够接受可迭代对象
A, B = zip(*zip(X, Y))
