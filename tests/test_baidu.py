import unittest
from time import sleep

from selenium import webdriver


# 综合练习：web自动化测试
# 1、类方法的使用
# 2、模块化、参数化
# 3、单元测试框架
# 此处:测试用例的断言不建议封装

class TestBaidu(unittest.TestCase):
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
        sleep(2)

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


if __name__ == '__main__':
    unittest.main()
