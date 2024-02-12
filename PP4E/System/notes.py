"""
@File         : nots.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-10 23:54:33
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st

st.set_page_config(layout="wide")
st.title("系统工具")
st.header("系统编程概述")
st.subheader("字符串方法基本知识")
st.write(
    """
    `find` 函数返回子字符串第一个匹配所在的偏移位置，`replace` 函数则是完全全局搜索和替换。
    """
)
st.header("介绍 `sys` 模块")

st.subheader("异常的详细信息")
st.write(
    """
    sys 模块中的其他属性允许我们获取与最近引发的 Python 异常相关的所有信息。 如果我们想以更通用的方式处理异常，这会很方便。
    
    例如，`sys.exc_info` 函数返回一个包含最新异常的类型、值和回溯对象的元组。
    """
)

st.header("介绍 `os` 模块")
st.subheader("常见 `os.path` 工具")
st.write(
    """
    内嵌的 `os.path` 模块提供了一整套目录处理相关工具。
    
    `os.path.isdir` 和 `os.path.isfile` 调用告诉我们文件名是目录还是简单文件；如果指定的文件不存在（即不存在意味着否定），则两者都返回 False。我们还收到了拆分和连接目录路径字符串的请求，这些字符串会自动使用运行 Python 的平台上的目录名称约定。
    """
)

st.write(
    """
    `os.path.split` 将文件名与其目录路径分开，而 `os.path.join` 将它们重新组合在一起 - 所有这些都使用调用它们的计算机的路径约定以完全可移植的方式进行。 此处的 `dirname` 和 `basename` 调用返回 `split` 返回的第一个和第二个项目，只是为了方便起见，并且 `splitext` 会去除文件扩展名（在最后一个 . 之后）。 微妙之处：它几乎等同于使用可移植 `os.sep` 字符串的字符串 `split` 和 `join` 方法调用，但不完全一样。
    
    如果您的路径变成一堆 Unix 和 Windows 分隔符，则 `normpath` 调用会派上用场。
    
    该模块还有一个绝对路径调用，可移植地返回文件的完整目录路径名； 它负责将当前目录添加为路径前缀以及.. 父语法等。
    """
)
st.subheader("在脚本里运行 shell 命令")
st.markdown("#### shell 命令是什么")
st.write(
    """
    术语“shell”是指在计算机上读取和运行命令行字符串的系统，“shell 命令”是指您通常在计算机的 shell 提示符下输入的命令行字符串。
    """
)
