"""
@File         : ch03_lists_versus_tuples.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-03-02 16:29:18
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""

import streamlit as st

st.set_page_config(layout="wide")
st.title("列表和元组")
st.subheader("Stephen CUI")
st.subheader("2024-03-01")
st.image(
    "figure/list_overallocation.png",
    caption="显示有多少额外元素被分配给特定大小的列表的图表。 例如，如果您使用追加创建一个包含 8,000 个元素的列表，Python 将为大约 8,600 个元素分配空间，从而过度分配了 600 个元素！",
)
st.image("img/fig3-3.png", caption="一个列表在多次添加时的变化示例")
