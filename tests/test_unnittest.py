import unittest

from calculator import Calculator


# 待验证：引入单元测试框架unittest 可避免 在错误出现时 后续函数可继续执行

# 测试用例规则：
# 1、创建测试类，并继承 unittest.TestCase
# 2、创建测试方法，必须以 test 开头
# 测试用例前置、后置动作
# suit = unittest.TestSuite()  测试套件（用于测试一组测试用例）
# suit.addTest(TestCalculator("test_add")) addTest可用于调整方法的执行顺序，默认是按照方法名称的ascii码先后顺序来执行
# runner = unittest.TextTestRunner()  测试运行器，可用于执行 runner.run(suit)


class TestCalculator(unittest.TestCase):
    """  单元测试框架、测试套件 """

    # 测试用例前置动作
    def setUp(self):
        print("----start----")

    # 测试用例后置动作
    def tearDown(self):
        print("----end----")

    def test_add(self):
        print("=====test_add=======")
        c = Calculator(1, 1)
        num = c.add()
        self.assertEqual(num, 2)

    def test_sub(self):
        print("=====test_sub=======")
        c = Calculator(1, 1)
        num = c.sub()
        self.assertEqual(num, 0)

    def test_mul(self):
        print("=====test_mul=======")
        c = Calculator(1, 1)
        num = c.mul()
        self.assertEqual(num, 1)

    def test_div(self):
        print("=====test_div=======")
        c = Calculator(1, 1)
        num = c.div()
        self.assertEqual(num, 1)


if __name__ == '__main__':
    # unittest.main()
    # 创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(TestCalculator("test_add"))
    suit.addTest(TestCalculator("test_sub"))
    suit.addTest(TestCalculator("test_mul"))
    suit.addTest(TestCalculator("test_div"))
    # 创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)
