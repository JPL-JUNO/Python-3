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
        "目录内容",
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
with tabs[5]:
    st.markdown(
        """
    ```python
    >>> import pathlib
    >>> 
    ```
    每个 `Path` 实例都包含用于处理其引用的文件内容的方法。 要立即检索内容，请使用 `read_bytes()` 或 `read_text()`。 要写入文件，请使用 `write_bytes()` 或 `write_text()`。 使用 `open()` 方法打开文件并保留文件句柄，而不是将名称传递给内置 `open()` 函数。
    ```python
    >>> f = pathlib.Path("example.txt")
    >>> f.write_bytes("This is the content".encode("utf-8"))
    19
    >>> with f.open("r", encoding="utf-8") as handle:
    ...     print(f"read from open() : {handle.read()!r}")
    ...
    read from open() : 'This is the content'
    >>> print(f"read text() : {f.read_text(encoding='utf-8')!r}")
    read text() : 'This is the content'
    >>>
    ```
    这些便捷方法在打开文件并写入文件之前会进行一些类型检查，但除此之外它们相当于直接执行操作。
    """
    )
with tabs[6]:
    st.markdown(
        """
    ```python
    >>> import pathlib
    >>>
    ```
    表示不存在的目录或符号链接的路径可用于创建关联的文件系统条目。 如果路径已经存在，`mkdir()` 会引发 `FileExistsError`。
    
    ```python
    >>> p = pathlib.Path("example_dir")
    >>> print(f"Creating {p}")
    Creating example_dir
    >>> p.mkdir()
    >>>
    ```
    
    使用 `symlink_to()` 创建符号链接。 该链接将根据路径的值命名，并将引用作为 `symlink_to()` 参数给出的名称。
    
    ```python
    >>> import pathlib
    >>>
    >>> p = pathlib.Path("example_link")
    >>> p.symlink_to("index.rst")
    >>> print(p)
    example_link
    >>> print(p.resolve().name)
    index.rst
    >>>
    ```
    如果遇到了，`OSError: [WinError 1314] 客户端没有所需的特权。: 'index.rst' -> 'example_link'`，则需要以管理员的方式运行。
    """
    )
with tabs[7]:
    st.markdown(
        """
    ```python
    >>> import pathlib
    >>>
    ```
    `Path` 实例包含多种用于测试路径引用的文件类型的方法。
    ```python
    import itertools, os, pathlib

    root = pathlib.Path("test_files")
    # Clean up from previous runs.
    if root.exists():
        for f in root.iterdir():
            f.unlink()
    else:
        root.mkdir()
    # Create test files.
    (root / "file").write_text("This is a regular file", encoding="utf-8")
    (root / "symlink").symlink_to("file")
    os.mkdir(str(root / "fifo"))
    # Check the file types.
    to_scan = itertools.chain(
        root.iterdir(), [pathlib.Path("/dev/disk0"), pathlib.Path("/dev/console")]
    )
    hfmt = "{:20s}" + (" {:>5}" * 6)
    print(hfmt.format("Name", "File", "Dir", "Link", "FIFO", "Block", "Character"))

    print()
    fmt = "{:20s}" + (" {!r:>5}" * 6)
    for f in to_scan:
        print(
            fmt.format(
                str(f),
                f.is_file(),
                f.is_dir(),
                f.is_symlink(),
                f.is_fifo(),
                f.is_block_device(),
                f.is_char_device(),
            )
        )
    ```
    """
    )
with tabs[8]:
    st.markdown(
        """
    ```python
    >>> import pathlib
    >>>
    ```
    可以使用 `stat()` 和 `lstat()` 方法访问有关文件的详细信息（用于检查可能是符号链接的状态）。这些方法分别产生与 `os.stat()` 和 `os.lstat()` 相同的结果。
    
    ```python
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
    ```
    为了更简单地访问有关文件所有者的信息，请使用 `owner()` 和 `group()`。
    ```python
    p = pathlib.Path(__file__)
    print(f"{p} is owned by {p.owner()} / {p.group()}")
    # windows is unsupported
    ```
    `touch()` 方法的工作方式类似于 Unix 命令 touch 来创建文件或更新文件现有文件的修改时间和权限。
    ```python
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
    ```
    """
    )

with tabs[9]:
    st.markdown(
        """
    在类 Unix 系统上，可以使用 `chmod()` 更改文件权限，并将模式作为整数传递。 众数可以使用 stat 模块中定义的常量来构造。
    
    ```python
    import os, pathlib, stat

    f = pathlib.Path("pathlib_chmod_example.txt")
    if f.exists():
        f.unlink()

    f.write_text("contents")
    # Determine which permissions are already set using stat.
    existing_permissions = stat.S_IMODE(f.stat().st_mode)
    print(f"Before: {existing_permissions:o}")
    # Decide which way to toggle them.
    if not (existing_permissions & os.X_OK):
        print("Adding execute permission")
        new_permissions = existing_permissions | stat.S_IXUSR
    else:
        print("Removing execute permission")
        new_permissions = existing_permissions ^ stat.S_IXUSR

    # Make the change and show the new value.
    f.chmod(new_permissions)
    after_permissions = stat.S_IMODE(f.stat().st_mode)
    print(f"After: {after_permissions:o}")
    ```
    """
    )
with tabs[10]:
    st.markdown(
        """
    ```python
    >>> import pathlib
    >>>
    ```
    根据类型，有两种方法可用于从文件系统中删除内容。要删除空目录，请使用 `rmdir()`。
    ```python
    >>> p = pathlib.Path("example_dir")
    >>> print(f"Removing {p}")
    Removing example_dir
    >>> p.rmdir()
    >>>
    ```
    如果已满足后置条件且目录不存在，则会引发 `FileNotFoundError` 异常。如果尝试删除不为空的目录，也会发生错误。
    
    对于文件、符号链接和大多数其他路径类型，请使用 `unlink()`。
    ```python
    >>> p = pathlib.Path("touched")
    >>> p.touch()
    >>> print("exists before removing:", p.exists())
    exists before removing: True
    >>> p.unlink()
    >>> print("exists after removing:", p.exists())
    exists after removing: False
    >>>
    ```
    """
    )
