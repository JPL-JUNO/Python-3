"""
@Title: 
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 16:37:31
@Description: 
"""

import unittest
import my_math1


class ProductTestCase(unittest.TestCase):
    def test_integers(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                p = my_math1.product(x, y)
                self.assertEqual(p, x * y, "Integer multiplication failed")

    def test_floats(self):
        for x in range(-10, 10):
            for y in range(-10, 10):
                x = x / 10
                y = y / 10
                p = my_math1.product(x, y)
                self.assertEqual(p, x * y, "Float multiplication failed")


if __name__ == "__main__":
    # unittest.main()负责替你运行测试：实例化所有的 TestCase 子类
    # 并运行所有名称以 test 打头的方法
    unittest.main()
# 如果你定义了方法setUp和tearDown，它们将分别在每个测试方法之前和之后执行。你可
# 使用这些方法来执行适用于所有测试的初始化代码和清理代码，这些代码称为测试夹具
# （test fixture）。
