import unittest


# def setUpModule():  在整个模块的开始执行
# @classmethod   用于类方法上
#     def setUpClass(cls):  在测试类开始和结束时执行

# def setUp(self):  前置方法,在该类中以test开头的方法（测试用例）前后都会被执行
# @unittest.skip("直接跳过测试")  跳过该测试方法的执行

def setUpModule():
    print("-----model-setUpModule-----")


def tearDownModule():
    print("-----model-tearDownModule-----")


class MyTest(unittest.TestCase):
    """  model、class、case之启动结束方法执行 """

    @classmethod
    def setUpClass(cls):
        print("-----class-setUpClass-----")

    @classmethod
    def tearDownClass(cls):
        print("-----class-tearDownClass-----")

    def setUp(self):
        print("-----test-case-setUp-----")

    def tearDown(self):
        print("-----test-case-tearDown-----")

    def test_case1(self):
        print("-----test_case1-----")

    @unittest.skip("直接跳过测试")
    def test_case2(self):
        print("-----test_case2-----")

    def case3(self):
        print("-----case3-----")


if __name__ == '__main__':
    unittest.main()
