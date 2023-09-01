"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-08-31 14:48:39
@Description: 关于 super()，一个有些令人惊讶的方面是，它并不是一定要关联到某个类的直接父类上，甚至可以在没有直接父类的类中使用它。
"""


class A:
    def spam(self):
        print("A.spam")
        super().spam()


class B:
    def spam(self):
        print("B.spam")


class C(A, B):
    pass


if __name__ == "__name__":
    c = C()
    c.spam()
    # 这一切都可以用类 C 的 MRO 列表来解释：
    C.__mro__
# 类 A 中使用的 super().spam()实际上居然调用到了类 B 中的 spam()
# 方法——B 和 A 是完全不相关的

# 是不是可以这样理解，super() 调用的只是 __mro__中上一级的方法
