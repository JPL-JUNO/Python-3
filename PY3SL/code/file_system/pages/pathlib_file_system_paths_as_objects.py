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

with tabs[2]:
    st.markdown(
        """
    ```python
    >>> import pathlib
    >>>
    ```
    路径对象具有用于从名称中提取部分值的方法和属性。 例如，`parts` 属性生成基于路径分隔符值解析的路径段序列。
    
    
    ```python
    >>> p = pathlib.PurePosixPath("/usr/local")
    >>> print(p.parts)
    ('/', 'usr', 'local')
    >>>
    ```
    
    有两种方法可以从给定路径对象“向上”导航文件系统层次结构。 `parent` 属性引用包含路径（该值由 `os.path.dirname()` 返回）的目录的新路径实例，。 `parents` 属性是一个可迭代对象，它生成父目录引用，不断“向上”路径层次结构，直到到达根目录。
    
    ```python
    >>> p = pathlib.PurePosixPath("/usr/local/lib")
    >>>
    >>> print(f"parent: {p.parent}")
    parent: /usr/local
    >>> print("Hierarchy:")
    Hierarchy:
    >>> for up in p.parents:
    ...     print(up)
    ... 
    /usr/local
    /usr
    /
    >>>
    ```
    路径的其他部分可以通过路径对象的属性来访问。`name` 属性保存路径的最后部分，位于最终路径分隔符之后（与 `os.path.basename()` 生成的值相同）。`suffix` 属性保存扩展名分隔符之后的值，`stem` 属性保存后缀之前的名称部分。
    
    ```python
    >>> p = pathlib.PurePosixPath("./source/pathlib/pathlib_name.py")
    >>>
    >>> print(f"path   : {p}")
    path   : source/pathlib/pathlib_name.py
    >>> print(f"name   : {p.name}")
    name   : pathlib_name.py
    >>> print(f"suffix : {p.suffix}")
    suffix : .py
    >>> print(f"stem   : {p.stem}")
    stem   : pathlib_name
    >>>
    ```
    """
    )

with tabs[3]:
    st.markdown(
        """
    ```python
    >>> import pathlib
    >>>
    ```
    具体 `Path` 类的实例可以从引用文件系统上的文件、目录或符号链接的名称（或潜在名称）的字符串参数创建。
    
    ```python
    >>> home = pathlib.Path.home()
    >>> print("home:", home)
    home: C:\\Users\\JPL-JUNO
    >>> cwd = pathlib.Path.cwd()
    >>> print("cwd:", cwd)
    cwd: D:\\Python-3\\PY3SL
    >>>
    ```
    """
    )

with tabs[4]:
    st.markdown(
        """
    ```python
    >>> import pathlib
    >>>
    ```
    
    可以使用三种方法来访问目录列表并发现文件系统上可用的文件名称。`iterdir()` 是一个生成器，为包含目录中的每个项目生成一个新的 `Path` 实例。
    
    ```python
    >>> import pathlib
    >>> p = pathlib.Path(".")
    >>> for f in p.iterdir():
    ...     print(f)
    ... 
    ospath_abspath.py
    ospath_basename.py
    ospath_commonpath.py
    ospath_commonprefix.py
    -- snipped --
    ```
    如果 `Path` 不表示目录，`iterdir()` 会引发 `NotADirectoryError`。
    
    使用 `glob()` 仅查找与模式匹配的文件。
    ```python
    >>> p = pathlib.Path(".")
    >>> for f in p.glob("*.rst"):
    ...     print(f)
    ...
    >>>
    ```
    `glob` 处理器支持使用模式前缀 `**` 或通过调用 `rglob()` 而不是 `glob()` 进行递归扫描。
    ```python
    >>> p = pathlib.Path("../")
    >>> for f in p.rglob("*.py"):
    ...     print(f)
    ... 
    ..\\file_system.py
    ..\\pages\\os.path_platform-independent_manipulation_of_filenames.py
    ..\\pages\\pathlib_file_system_paths_as_objects.py
    ..\\source\\ospath_abspath.py
    ..\\source\\ospath_basename.py
    -- snipped
    ```
    """
    )
