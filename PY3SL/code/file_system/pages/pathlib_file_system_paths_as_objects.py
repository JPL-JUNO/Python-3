"""
@File         : pathlib File System Paths as Objects.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-23 22:35:37
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st

st.set_page_config(layout="wide")

st.title("pathlib: 文件系统路径作为对象")
st.subheader("Stephen CUI")
st.subheader("2024-02-22 22:22:11")
st.write(
    "`pathlib` 模块提供了一个面向对象的 API，用于解析、构建、测试以及以其他方式处理文件名和路径，而不是使用低级字符串操作。"
)
tabs = st.tabs(
    [
        "路径表示",
        "建立路径",
        "解析路径",
        "创建具体路径",
        "目录类容",
        "读写文件",
        "管理目录和符号链接",
        "文件类型",
        "文件属性",
        "权限",
        "删除",
    ]
)

with tabs[0]:
    st.markdown(
        """
        `pathlib` 包含用于管理使用 POSIX 标准或 Microsoft Windows 语法格式化的文件系统路径的类。它包括“纯”类（对字符串进行操作但不与实际文件系统交互）和“具体”类（将 API 扩展为包括反映或修改本地文件系统上的数据的操作）。

        纯类 `PurePosixPath` 和 `PureWindowsPath` 可以在任何操作系统上实例化和使用，因为它们仅适用于名称。要实例化正确的类以使用真实的文件系统，请使用 `Path` 获取 `PosixPath` 或 `WindowsPath`，具体取决于平台。
    """
    )
with tabs[1]:
    st.markdown(
        """
        ```python
        >>> import pathlib
        >>> 
        ```
        要实例化新路径，请将字符串作为第一个参数。 路径对象的字符串表示形式就是该名称值。 要创建引用相对于现有路径的值的新路径，请使用 / 运算符扩展路径。 运算符的参数可以是字符串或另一个路径对象。
        
        ```python
        >>> usr = pathlib.PurePosixPath("/usr")
        >>> print(usr)
        /usr
        >>>
        >>> usr_local = usr / "local"
        >>> print(usr_local)
        /usr/local
        >>>
        >>> usr_share = usr / pathlib.PurePosixPath("share")
        >>> print(usr_share)
        /usr/share
        >>>
        >>> root = usr / ".."
        >>> print(root)
        /usr/..
        >>>
        >>> etc = root / "/etc/"
        >>> print(etc)
        /etc
        >>>
        ```
        正如示例输出中 `root` 的值所示，运算符将给定的路径值组合在一起，并且当结果包含父目录引用 “..” 时，不会对结果进行标准化。 但是，如果段以路径分隔符开头，则它会被解释为新的“根”引用，方式与 `os.path.join()` 相同。 额外的路径分隔符将从路径值的中间删除，如此处的 `etc` 示例所示。
        
        具体路径类包括一个 `resolve()` 方法，用于通过查看文件系统中的目录和符号链接并生成名称引用的绝对路径来标准化路径。
        
        ```python
        >>> usr_local = pathlib.Path("/usr/local")
        >>> share = usr_local / ".." / "share"
        >>> print(share.resolve())
        C:\\usr\\share
        >>>
        ```
        要在事先未知路径段的情况下构建路径，请使用 `joinpath()`，将每个路径段作为单独的参数传递。与 / 运算符一样，调用 joinpath() 会创建一个新实例。
        ```python
        >>> root = pathlib.PurePosixPath("/")
        >>> subdirs = ["usr", "local"]
        >>> usr_local = root.joinpath(*subdirs)
        >>> print(usr_local)
        /usr/local
        >>>
        ```
        
        给定一个现有的路径对象，很容易构建一个具有细微差别的新路径对象，例如引用同一目录中的不同文件。 使用 `with_name()` 创建一个新路径，用不同的文件名替换路径的名称部分。 使用 `with_suffix()` 创建一个新路径，用不同的值替换文件名的扩展名。这两个方法都返回新对象，原来的对象仍保持不变。
        
        ```python
        >>> ind = pathlib.PurePosixPath("source/pathlib/index.rst")
        >>> print(ind)
        source/pathlib/index.rst
        >>> py = ind.with_name("pathlib_from_existing.py")
        >>> print(py)
        source/pathlib/pathlib_from_existing.py
        >>> pyc = py.with_suffix(".pyc")
        >>> print(pyc)
        source/pathlib/pathlib_from_existing.pyc
        >>>
        ```
    """
    )
