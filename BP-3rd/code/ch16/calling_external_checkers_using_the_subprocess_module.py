"""
@Title: 使用模块subprocess调用外部检查器
@Author(s): Stephen CUI
@LastEditor(s): Stephen CUI
@CreatedTime: 2023-09-04 17:02:52
@Description: 
"""

import unittest
import my_math
from subprocess import Popen, PIPE


class ProductTestCase(unittest.TestCase):
    # def test_with_PyCheck(self):
    #     cmd = 'pychecker', '-Q', my_math.__file__.rstrip('c')
    #     pychecker = Popen(cmd, stdout=PIPE, stderr=PIPE)
    #     self.assertEqual(pychecker.stdout.read(), '')

    def test_with_PyLint(self):
        cmd = 'pylint', '-rn', 'my_math'
        pylint = Popen(cmd, stdout=PIPE, stderr=PIPE)
        print(pylint.stdout.read())
        self.assertEqual(pylint.stdout.read(), b'')
        # 修改前
        # self.assertEqual(pylint.stdout.read(), '')


if __name__ == '__main__':
    unittest.main()
