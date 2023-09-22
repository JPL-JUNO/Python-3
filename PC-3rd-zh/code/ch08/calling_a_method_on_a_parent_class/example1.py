"""
@Title: 调用父类中的方法
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 14:21:58
@Description: 
"""


class A:
    def spam(self):
        print("A.spam()")


class B(A):
    def spam(self):
        print("B.spam()")
        super().spam()  # Call parent spam()
