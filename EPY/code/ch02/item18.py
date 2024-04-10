"""
@File         : item18.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-10 22:39:43
@Email        : cuixuanstephen@gmail.com
@Description  : 学会利用 __missing__ 构造依赖键的默认值
"""

pictures = {}
path = "profile_1234.png"

if (handle := pictures.get(path)) is None:
    # 当文件句柄已存在于字典中时，此代码仅进行单个字典访问。
    # 如果文件句柄不存在，则通过 get 访问字典一次，
    # 然后在 try/ except 块的 else 子句中对其进行赋值。
    try:
        handle = open(path, "a+b")
    except OSError:
        print(f"Failed to open path {path}")
    else:
        pictures[path] = handle

handle.seek(0)
image_data = handle.read()
