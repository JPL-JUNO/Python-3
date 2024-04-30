"""
@File         : 6_5_enhanced_generators_and_yield_expressions.py
@Author(s)    : Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime  : 2024-04-21 14:16:47
@Email        : cuixuanstephen@gmail.com
@Description  : 
"""


def receiver():
    print("Ready to receive")
    while True:
        n = yield
        print("Got", n)


r = receiver()
r.send(None)  # 将执行流程定位到生成器中 yield 第一次执行的位置
r.send(1)
r.send(2)
r.send("Hello, yield")
