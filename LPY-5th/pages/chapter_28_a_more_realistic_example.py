import streamlit as st

st.title(":violet[一个更加实际的示例]")
st.subheader("[Stephen CUI](https://github.com/JPL-JUNO)")
st.subheader("2024-02-26")
tabs = st.tabs(["使用内省工具", "把对象存储到数据库中"])
with tabs[0]:
    st.markdown(
        """
    内置的 `instance.__class__` 属性提供了一个从实例到创建它的类的链接。类反过来有一个 `__name__` （就像模块一样），还有一个 `__bases__` 序列，提供了超类的访问。我们使用这些来打印创建一个实例的类的名字，而不是通过硬编码来做到。

    内置的 `object.__dict__` 属性提供了一个字典，带有一个键/值对，以便每个属性都附加到一个命名控件对象（包括模块、类和实例）。由于它是字典，因此我们可以获取键的列表、按照键来索引、迭代其键，等等，从而广泛地处理所有的属性。我们使用这些来打印出任何实例的每个属性，而不是在定制显示中硬编码。
    ```python
    >>> from step4 import Person
    >>>
    >>> bob = Person("Bob Smith")
    >>> bob  # Show bob's __repr__ (not __str__)
    [Person: Bob Smith, 0]
    >>> print(bob)  # Ditto: print => __str__ or __repr__
    [Person: Bob Smith, 0]
    >>> bob.__class__  # Show bob's class and its name
    <class 'step4.Person'>
    >>> bob.__class__.__name__
    'Person'
    >>> list(bob.__dict__.keys())  # Attributes are really dict keys
    ['name', 'job', 'pay']
    >>> for key in bob.__dict__:  # Index manually
    ...     print(key, " => ", bob.__dict__[key])
    ...
    name  =>  Bob Smith
    job  =>  None
    pay  =>  0
    >>> for key in bob.__dict__:  # obj.attr, but attr is a var
    ...     print(key, " => ", getattr(bob, key))
    ...
    name  =>  Bob Smith
    job  =>  None
    pay  =>  0
    >>> 
    ```
    如果一个实例的类定义了 `__slots__`，而实例可能没有存储在 `__dict__` 字典中，但实例的一些属性也是可以访问的，这是新式类（以及 Python 3.0 中的所有类）的一项可选的和相对不太明确的功能，即把属性存储在数组中。既然 `slots` 其实属于类而不是实例，并且它们在任何事件中极少用到，那么我们在这里可以忽略它们而关注常规的 `__dict__`。
    
    然而我们也必须记住，某些程序可能需要为一个缺省的 `__dict__` 捕获异常，如果其用户要展示 `slot` 的话应使用 `hasattr` 来测试或使用带默认的 `getattr`。
    
    ### 实例:vs:类属性
    继承的类属性只是附加到了类，而没有向下复制到实例。
    ### 工具类的命名要求
    Python 程序员常常对于不想做其他用途的方法添加一个单个下划线的前缀。一种更好的但不太常用的方法是，只在方法名前面使用两个下划线符号。
    """
    )

with tabs[1]:
    st.markdown(
        """
    ### Pickle 和 Shelve
    对象持久化通过 3 个标准的库模块来实现，这 3 个模块在 Python 中都可用：
    - pickle: 任意 Python 对象和字节串之间的序列化
    - dbm: 实现一个可通过键访问的文件系统，以存储字符串
    - shelve: 使用另两个模块按照键把 Python 对象存储到一个文件中
    #### pickle 模块
    pickle 模块是一种非常通用的对象格式化和解格式化工具：对于内存中几乎任何的 Python 对象，它都能聪明地把对象转换为字节串，这个字节串可以随后用来在内存中重新构建最初的对象。pickle 模块几乎可以处理我们所能够创建的任何对象，包括列表、字典、嵌套组合以及类实例。后者对于 pickle 来说特别有用，因为它们提供了数据（属性）和行为（方法），实际上，组合几乎等于“记录”和“程序”。由于 pickle 如此通用，所以我们可以不用编写代码来创建和解析对象的定制文本文件表示，它可以完全替代这些代码。通过在文件中存储一个对象的 pickle 字符串，我们可以有效地使其持久。
    #### shelve 模块
    尽管使用 pickle 本身把对象存储为简单的普通文件并随后载入它们是很容易的，但 shelve 模块提供了一个额外的层结构，允许按照键来存储 pickle 处理后的对象。shelve 使用 pickle 把一个对象转换为其 pickle 化的字符串，并将其存储在一个 dbm 文件中的键之下；随后载入的时候，shelve 通过键获取 pickle 化的字符串，并用 pickle 在内存中重新创建最初的对象。这都很有技巧，但是，对于脚本来说，一个 shelve 的 pickle 化的对象看上去就像是字典——我们通过键索引来访问、指定键来存储，并且使用 len、in 和 dict.keys 这样的字典工具来获取信息。Shelve 自动把字典操作映射到存储在文件中的对象。
    ### 在 shelve 数据库中存储对象
    """
    )
