"""
@File         : chapter_29_class_coding_details.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-28 21:10:51
@Email        : cuixuanstephen@gmail.com
@Description  : 类代码编写细节
"""

import streamlit as st

st.set_page_config(layout="wide")
st.title(":red[类代码编写细节]")
st.subheader("[Stephen CUI](https://github.com/JPL-JUNO)")
st.subheader("2024-02-28")
tabs = st.tabs(["class 语句", "方法", "继承"])
with tabs[0]:
    st.markdown(
        """
    ### 一般形式
    `class` 是复合语句，其缩进语句的主体一般都出现在头一行下边。在头一行中，父类列在类名称之后的括号内，由逗号相隔。列出一个以上的父类会引起多重继承。以下是 `class` 语句的一般形式：
    ```python
    class <name>(superclass, ...): # Assign to name
        attr = value # Shared class data
        def method(self, ...): # Methods
            self.attr = value # Per-instance data
    ```
    ```python
    >>> class SharedData:
    ...     spam = 42  # Generates a class data attribute
    ... 
    >>> 
    >>> x = SharedData()  # Make two instances
    >>> y = SharedData()
    >>> x.spam, y.spam  # They inherit and share 'spam' (a.k.a. SharedData.spam)
    (42, 42)
    >>> SharedData.spam = 99
    >>> x.spam, y.spam, SharedData.spam
    (99, 99, 99)
    ```
    对实例的属性进行赋值运算会在该实例内创建或修改变量名，而不是在共享的类中。通常的情况下，继承搜索只会在属性引用时发生，而不是在赋值运算时发生：对对象属性进行赋值总是会修改该对象，除此之外没有其他的影响。
    
    利用这些技术把属性储存在不同对象内，我们可以决定其可见范围。附加在类上时，变量名是共享的；附加在实例上时，变量名是属于每个实例的数据，而不是共享的行为或数据。虽然继承搜索会查找变量名，但总是可以通过直接读取所需要的对象，而获得树中任何地方的属性。
    """
    )
with tabs[1]:
    st.markdown(
        """
    方法位于 `class` 语句的主体内，是由 `def` 语句建立的函数对象。从抽象的视角来看，方法替实例对象提供了要继承的行为。从程序设计的角度来看，方法的工作方式与简单函数完全一致，只是有个重要差异：方法的第一个参数总是接收方法调用的隐性主体，也就是实例对象。
    
    换句话说，Python 会自动把实例方法的调用对应到类方法函数，如下所示。方法调用需通过实例，就像这样：
    ```python
    instance.methods(args...)
    ```
    这会自动翻译成以下形式的类方法函数调用：
    ```python
    class.method(instance, args...)
    ``` 
    ### 调用父类构造函数
    方法一般是通过实例调用的。不过，通过类调用方法也扮演了一些特殊的角色。常见的场景涉及了构造函数。就像所有属性 `__init__` 方法是由继承进行查找的。也就是说，在构造时，Python 会找出并且只调用一个 `__init__`。如果要保证子类的构造函数也会执行父类构造时的逻辑，一般都必须通过类明确地调用父类的 `__init__` 方法。
    ### 其他方法调用的可能性
    这种通过类调用方法的模式是扩展（而不是完全替换）继承的方法行为的一般基础。它需要传递一个显式实例，因为所有方法默认都会传递。从技术上讲，这是因为方法是没有任何特殊代码的实例方法。
    
    静态方法，可让你编写不预期第一参数为实例对象的方法。这类方法可像简单的无实例的函数那样运作，其变量名属于其所在类的作用域，并且可以用来管理类数据。类方法，当调用的时候接受一个类而不是一个实例，并且它可以用来管理基于每个类的数据。
    """
    )

with tabs[2]:
    st.markdown(
        """
    在 Python 中，当对对象进行点号运算时，就会发生继承，而且涉及了搜索属性定义树。每次使用 `object.attr` 形式的表达式时（object 是实例或类对象），Python 会从头至尾搜索命名空间树，先从对象开始，寻找所能找到的第一个 attr。这包括在方法中对 self 属性的引用。因为树中较低的定义会覆盖较高的定义，继承构成了专有化的基础。
    ### 属性树的构造
    """
    )
    st.image(
        "./img/fig29-1.png",
        caption="程序代码会在内存中创建对象树，这个树是通过属性继承搜索的。调用类会创建记忆了这个类的新的实例。执行 class 语句会创建新的类，而列在 class 语句首行括号内的类则成为父类。即使 self 属性位于类的方法内每个属性引用，都会触发由下至上的树搜索",
    )
    st.markdown(
        """
    通常来说：
    - 实例属性是由对方法内 self 属性进行赋值运算而生成的。
    - 类属性是通过 class 语句内的语句（赋值语句）而生成的。
    - 父类的连接是通过 class 语句首行的括号内列出类而生成的。
    
    结果就是连接实例的属性命名空间树，到产生它的类、再到类首行中所列出的所有父类。每次以点号运算从实例对象取出属性名称时，Python 会向上搜索树，从实例直到父类。
    
    ### 定制被继承的方法 
    """
    )
