import unittest
from time import sleep

from selenium import webdriver

from baidu_page import BaiduPage


# 注意：使用存在部分问题
# page = BaiduPage(self.driver)
# page.get("https://www.baidu.com")   报错
# 此处获取的page元素 无法调用click()等方法

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.base_url = "https://www.baidu.com"

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()

    def test_baidu_search(self):
        page = BaiduPage(self.driver)
        # page.get("https://www.baidu.com")   报错
        self.driver.get("https://www.baidu.com")
        page.search_input = "page object"
        print("---success---")


if __name__ == '__main__':
    unittest.main(verbosity=2)
