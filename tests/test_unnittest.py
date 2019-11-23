import unittest

from calculator import Calculator


# 引入单元测试框架unittest 可避免 在错误出现时 后续函数可继续执行
# 测试用例规则：
# 1、创建测试类，并继承 unittest.TestCase
# 2、创建测试方法，必须以 test 开头

class TestCalculator(unittest.TestCase):

    def test_add(self):
        c = Calculator(1, 1)
        num = c.add()
        self.assertEqual(num, 2)

    def test_sub(self):
        c = Calculator(1, 1)
        num = c.sub()
        self.assertEqual(num, 0)

    def test_mul(self):
        c = Calculator(1, 1)
        num = c.mul()
        self.assertEqual(num, 1)

    def test_div(self):
        c = Calculator(1, 1)
        num = c.div()
        self.assertEqual(num, 1)


if __name__ == '__main__':
    unittest.main()
