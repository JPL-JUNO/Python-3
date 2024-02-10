"""
@File         : note.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-02-08 21:43:07
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st

st.set_page_config(layout="wide")

st.title("OOP: 宏伟蓝图")
st.header("概览 OOP")
st.subheader("属性继承搜索")
st.write(
    """
    在 Python 对象模型中，类和通过类产生的实例是两种不同的对象模型：
    
    **类** 类是实例工厂。类的属性提供了行为（数据以及函数），所有从类产生的实例都继承了该类的属性。
    
    **实例** 代表程序领域中具体的元素。实例的属性记录了每个实例自己的数据。
    """
)

st.subheader("方法调用")
st.write(
    """
    方法可以通过实例 `bob.giveRaise()` 或类 `Employee.giveRaise(bob)` 来调用，这两种形式都可以在我们的脚本中发挥作用。这些调用还说明了 OOP 中的两个关键思想：运行 `bob.giveRaise()` 方法调用，Python：
    
    1. 通过继承搜索从 bob 中查找 `giveRaise`
    2. 将 bob 传递给位于特殊 self 参数中的 `giveRaise` 函数

    当您调用 `Employee.giveRaise(bob)` 时，您只需自己执行这两个步骤。从技术上讲，此描述是默认情况（Python 还有其他方法类型），但它适用于用该语言编写的绝大多数 OOP 代码。
    """
)
st.subheader("编写树类")
st.write(
    """
    从操作的角度来看，当 def 出现在类的内部时，通常称为方法。而且会自动接收第一个特殊参数（按照惯例称为 self），
    这个参数提供了被处理的实例的引用。所有你自己向方法中传入的参数都被赋给了 self 后面的参数。
    """
)
