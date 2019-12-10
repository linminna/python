import unittest
from time import sleep

from selenium import webdriver

from baidu_base_page import BaiduPage as Bp
from baidu_poium_page import BaiduPage


# 注意：使用存在部分问题
# page = BaiduPage(self.driver)
# page.get("https://www.baidu.com")

class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        sleep(2)
        cls.driver.quit()

    def test_baidu_basepage_search(self):
        page = Bp(self.driver)
        page.open("https://www.baidu.com")
        page.search_input("page object")
        page.search_button()
        sleep(2)
        self.assertEqual(self.driver.title, "page object_百度搜索")
        print("---test_baidu_basepage_search---success")

    def test_baidu_poium_search(self):
        page = BaiduPage(self.driver)
        page.get("https://www.baidu.com")
        page.search_input = "poium"
        page.search_button.click()
        sleep(2)
        self.assertEqual(page.get_title, "poium_百度搜索")
        print("---test_baidu_poium_search---success")


if __name__ == '__main__':
    unittest.main(verbosity=2)
