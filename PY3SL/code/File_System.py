"""
@File         : File_System.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-22 21:33:18
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st

st.subheader("Stephen CUI")
st.subheader("2024-02-22 21:33:18")

tabs = st.tabs(
    [
        "os.path: 平台独立的文件名管理",
        "pathlib: 文件系统路径作为对象",
        "glob: 文件名匹配模式",
        "fmmatch: UNIX 式 glob 模式匹配",
        "Linecache: 高效读取文本文件",
        "tempfile: 临时文件系统对象",
        "shutil: 高层文件操作",
        "filecmp: 文件比较",
        "mmap: 内存映射文件",
        "codecs: 字符串编码和解码",
        "io: 文本、十进制和原始流 I/O 工具",
    ]
)

with tabs[1]:
    pass
