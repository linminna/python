import os
import unittest
from time import sleep

from ddt import ddt, data, unpack, file_data
from parameterized import parameterized
from selenium import webdriver


# 综合练习：web自动化测试
# 1、类方法的使用
# 2、模块化、参数化
# 3、单元测试框架
# 安装parameterized、ddt  pip install
# 4、@parameterized([]) 参数化库的使用
# 5、@ddt注意在类上添加，否则在运行时会报错
# @data(("a1", "a11"), ("a2", "a22"))
#     @unpack
# 如果没有unpack，那么[a1,a11] 当成一个参数传入用例运行
# 如果有unpack，那么[a1,a11] 被分解开，按照用例中的两个参数传递
# 读取json文件作为参数列表  @file_data(parent_path + './file/ddt_data.json')
# 若要读取yml文件，需要先 pip install pyyaml，注意：此处开始安装时失败，后面在将pip升级后 安装成功。
# 获取当前文件的父目录  os.path.dirname(os.path.dirname(__file__))
# 当前文件所在目录  os.path.dirname(__file__)


# 此处:测试用例的断言不建议封装

@ddt
class TestBaidu(unittest.TestCase):
    """  综合案例：unittest、模块化与参数化 """

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys(search_key)
        self.driver.find_element_by_id("su").click()
        sleep(1)

    def test_search_key_selenium(self):
        search_key = "selenium"
        print(search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    def test_search_key_unittest(self):
        search_key = "unittest"
        print(search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @parameterized.expand([
        ("c1", "lmn"), ("c2", "hk")
    ])
    def test_search1(self, name, search_key):  # 此处，name对应元祖中第一个参数，search_key对应第二个
        print("----parameterized----" + search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # ddt 参数化使用1：元组
    @data(("a1", "a"), ("a2", "aa"))
    @unpack
    def test_search2(self, case, search_key):  # 此处，case对应元祖中第一个参数，search_key对应第二个
        print("---ddt-第一组---" + search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # ddt 参数化使用2：列表
    @data(["b1", "b"], ["b2", "bb"])
    @unpack
    def test_search3(self, case, search_key):  # 此处，case对应元祖中第一个参数，search_key对应第二个
        print("---ddt-第二组---" + search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    # ddt 参数化使用3：字典
    @data({"search_key": "p"}, {"search_key": "pp"})
    @unpack
    def test_search4(self, search_key):
        print("---ddt-第三组---" + search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    parent_path = os.path.dirname(os.path.dirname(__file__))
    print("--parent_path--" + parent_path)

    @file_data(parent_path + './file/ddt_data.json')
    def test_read_json(self, search_key):
        print("---ddt-第四组---" + search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")

    @file_data(parent_path + './file/ddt_data.yml')
    def test_read_yml(self, case):
        search_key = case[0]["search_key"]
        print("---ddt-第五组---" + search_key)
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + "_百度搜索")


if __name__ == '__main__':
    unittest.main(verbosity=2)  # verbosity=2 为输出详细日志，目前没看到区别
