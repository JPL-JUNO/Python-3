"""
@File         : os.path_Platform-Independent_Manipulation_of_Filenames.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-22 22:22:11
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st

st.title("os.path: 平台独立的文件名管理")
st.subheader("Stephen CUI")
st.subheader("2024-02-22 22:22:11")
tabs = st.tabs(["解析路径", "建立路径", "规范化路径", "文件时间", "测试文件"])
with tabs[0]:
    st.markdown(
        """
        ```python
        >>> import os.path
        >>>
        ```
        `os.path` 中的第一组函数可用于将表示文件名的字符串解析为其组成部分。 这些功能不依赖于实际存在的路径； 相反，它们仅对字符串进行操作。

        路径解析取决于 `os` 中定义的几个变量：
        - `os.sep`：路径各部分之间的分隔符（例如 “/” 或 “\”）。
        - `os.extsep`：文件名和文件“扩展名”之间的分隔符（例如 “.”）。
        - `os.pardir`：路径组件，表示向上遍历目录树一层（例如 “..”）。
        - `os.curdir`：引用当前目录的路径组件（例如 “.”）。

        `split()` 函数将路径分成两个独立的部分，并返回一个包含结果的元组。 元组的第二个元素是路径的最后一个组成部分，第一个元素是它之前的所有元素。
        
        ```python
        >>> PATHS = ["one/two/three", "/one/two/three/", "/", ".", ""]
        >>> for path in PATHS:
        ...     print(f"{path!r:>17} : {os.path.split(path)}")
        ...
          'one/two/three' : ('one/two', 'three')
        '/one/two/three/' : ('/one/two/three', '')
                      '/' : ('/', '')
                      '.' : ('', '.')
                       '' : ('', '')
        >>>
        ```
        输入的参数以 `os.sep` 结尾时，路径的最后一个元素是一个空串。
        
        `basename()` 函数返回的值相当于 `split()` 的第二部分值。
        ```python
        >>> PATHS = ["one/two/three", "/one/two/three/", "/", ".", ""]
        >>> for path in PATHS:
        ...     print(f"{path!r:>17} : {os.path.basename(path)!r}")
        ...
          'one/two/three' : 'three'
        '/one/two/three/' : ''
                      '/' : ''
                      '.' : '.'
                       '' : ''
        >>>
        ```
        完整路径被剥离到最后一个元素，无论它是指文件还是目录。 如果路径以目录分隔符 (`os.sep`) 结尾，则基本部分被视为空。
        
        `dirname()` 返回分解路径得到的第一部分。
        ```python
        >>> for path in PATHS:
        ...     print(f"{path!r:>17} : {os.path.dirname(path)!r}")
        ...
          'one/two/three' : 'one/two'
        '/one/two/three/' : '/one/two/three'
                      '/' : '/'
                      '.' : ''
                       '' : ''
        >>>
        ```
        将 `basename()` 与 `dirname()` 的结果相结合即可得出原始路径。
        
        `splitext()` 的工作方式与 `split()` 类似，但在扩展名分隔符上划分路径，而不是在目录分隔符上。
        ```python
        >>> PATHS = [
        ...     "filename.txt",
        ...     "filename",
        ...     "/path/to/filename.txt",
        ...     "/",
        ...     "",
        ...     "my-archive.tar.gz",
        ...     "no-extension.",
        ... ]
        >>> for path in PATHS:
        ...     print(f"{path!r:>21} : {os.path.splitext(path)}")
        ...
                 'filename.txt' : ('filename', '.txt')
                     'filename' : ('filename', '')
        '/path/to/filename.txt' : ('/path/to/filename', '.txt')
                            '/' : ('/', '')
                             '' : ('', '')
            'my-archive.tar.gz' : ('my-archive.tar', '.gz')
                'no-extension.' : ('no-extension', '.')
        >>>        
        ```
        查找扩展名时仅使用最后一次出现的 `os.extsep`。 因此，如果一个文件名有多个扩展名，则拆分的结果会在前缀上留下部分扩展名。
        
        `commonprefix()` 将路径列表作为参数，并返回一个字符串，该字符串表示所有路径中存在的公共前缀。 该值可能代表实际不存在的路径，并且不考虑路径分隔符。 因此，前缀可能不会停在分隔符边界上。
        ```python
        >>> paths = [
        ...     "/one/two/three/four",
        ...     "/one/two/threefold",
        ...     "/one/two/three/",
        ... ]
        >>> for path in paths:
        ...     print("PATH:", path)
        ...
        PATH: /one/two/three/four
        PATH: /one/two/threefold
        PATH: /one/two/three/
        >>> print("PREFIX:", os.path.commonprefix(paths))
        PREFIX: /one/two/three
        >>>
        ```
        有一个路径根本就不包含 `/one/two/three`。`commonpath()` 考虑路径分隔符。 它返回一个不包含部分的前缀路径值。
        ```python
        >>> print("PREFIX:", os.path.commonpath(paths))
        PREFIX: \one\\two
        >>>
        ```
    """
    )
with tabs[1]:
    st.markdown(
        """
        ```python
        >>> import os.path
        >>>
        ```
        要将多个路径组件组合成一个值，请使用 `join()`。
        ```python
        >>> PATHS = [
        ...     ("one", "two", "three"),
        ...     ("/", "one", "two", "three"),
        ...     ("/one", "/two", "/three"),
        ... ]
        >>> for parts in PATHS:
        ...     print(f"{parts} : {os.path.join(*parts)!r}")
        ...
        ('one', 'two', 'three') : 'one\\\\two\\\\three'
        ('/', 'one', 'two', 'three') : '/one\\\\two\\\\three'
        ('/one', '/two', '/three') : '/three'
        >>>
        ```
        如果 `join` 的某个参数以 `os.sep` 开头，则所有前面的参数都将被丢弃，该参数将成为返回值的开头。
        
        还可以使用包含可自动扩展的“可变”组件的路径。 例如，`expanduser()` 将波形符 (~) 字符转换为用户主目录的名称。
        
        ```python
        >>> for user in ["", "stephen", "nosuchuser"]:
        ...     lookup = "~" + user
        ...     print(f"{lookup!r:>15} : {os.path.expanduser(lookup)!r}")
        ... 
                    '~' : 'C:\\Users\\JPL-JUNO'
             '~stephen' : 'C:\\Users\\stephen'
          '~nosuchuser' : 'C:\\Users\\nosuchuser'
        >>> 
        ```
        如果找不到用户的主目录，则字符串原样返回。
        
        `expandvars()` 更通用，它扩展路径中存在的任何 `shell` 环境变量。
        ```python
        >>> os.environ["MYVAR"] = "VALUE"
        >>> os.path.expandvars("/path/to/$MYVAR")
        '/path/to/VALUE
        ```
        不执行任何验证来确保变量值产生的文件名已存在。
        """
    )
with tabs[2]:
    st.markdown(
        """
        ```python
        >>> import os.path
        >>>
        ```
        使用 `join()` 或嵌入变量从单独的字符串组装的路径可能最终会带有额外的分隔符或相对路径组件。 使用 `normpath()` 来清理它们。

        ```python
        >>> PATHS = [
        ...     "one//two//three",
        ...     "one/./two/./three",
        ...     "one/../alt/two/three",
        ... ]
        >>> for path in PATHS:
        ...     print(f"{path!r:>22} : {os.path.normpath(path)}")
        ...
             'one//two//three' : one\\two\\three
           'one/./two/./three' : one\\two\\three
        'one/../alt/two/three' : alt\\two\\three
        >>>
        ```
        由 `os.curdir` 和 `os.pardir` 组成的路径段被评估并折叠。
        
        要将相对路径转换为绝对文件名，使用 `abspath()`。
        
        ```python
        >>> os.chdir(os.path.expanduser("~"))
        >>> PATHS = [
        ...     ".",
        ...     "..",
        ...     "./one/two/three",
        ...     "../one/two/three",
        ... ]
        >>> for path in PATHS:
        ...     print(f"{path!r:>21} : {os.path.abspath(path)!r}")
        ...
                          '.' : 'C:\\Users\\JPL-JUNO'
                         '..' : 'C:\\Users'
            './one/two/three' : 'C:\\Users\\JPL-JUNO\\one\\two\\three'
           '../one/two/three' : 'C:\\Users\\one\\two\\three'
        >>>
        ```
      """
    )

with tabs[3]:
    st.markdown(
        """
        ```python
        import os.path
        import time
        ```
        除了使用路径之外，`os.path` 还包括用于检索文件属性的函数，类似于 `os.stat()` 返回的函数。
        ```python
        print("File         :", __file__)
        print("Access time  :", time.ctime(os.path.getatime(__file__)))
        print("Modified time:", time.ctime(os.path.getmtime(__file__)))
        print("Change time  :", time.ctime(os.path.getctime(__file__)))
        print("Size         :", os.path.getsize(__file__))
        ```
        
        `os.path.getatime() `返回访问时间，`os.path.getmtime()` 返回修改时间，`os.path.getctime()` 返回创建时间。 `os.path.getsize()` 返回文件中的数据量，以字节表示。
  """
    )
with tabs[4]:
    st.markdown(
        """
        当程序遇到路径名时，通常需要知道该路径是否引用文件、目录或符号链接以及是否存在。`os.path` 包含用于测试所有这些条件的函数。
        
        ```python
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
        ```
  """
    )
