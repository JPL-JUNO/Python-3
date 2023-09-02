"""
@Title: 头等对象 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-02 11:46:19
@Description: 可以利用该特性来编写非常紧凑和灵活的代码
"""

line = "ACME, 100, 490.10"
column_types = [str, int, float]
parts = line.split(", ")
row = [ty(val) for val, ty in zip(parts, column_types)]
print(row)

# 将函数或类放在字典中是消除复杂 if-elif-else 语句的常用技术


class TextFormatter:
    pass


class CSVFormatter:
    pass


class HTMLFormatter:
    pass


# ❌
if format == "text":
    formatter = TextFormatter()
elif format == "csv":
    formatter = CSVFormatter()
elif format == "html":
    formatter = HTMLFormatter()
else:
    raise RuntimeError("Bad format")

# ✅ 更加灵活，因为可以向字典中增加更多的项来添加新的情况
_formats = {
    "text": TextFormatter,
    "html": HTMLFormatter,
    "csv": CSVFormatter,
}
if format in _formats:
    formatter = _formats[format]()
else:
    raise RuntimeError("Bad format")
