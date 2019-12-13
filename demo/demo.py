import datetime
import time
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from demo_page import DemoPage


# 出发、到达城市的选择 元素定位？？

# 去哪儿网搜索单程机票
class TestQunaer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_demo(self):
        page = DemoPage(self.driver)
        page.get("https://flight.qunar.com/")
        single_way = page.single_way
        from_city = page.from_city
        to_city = page.to_city
        from_date = page.from_date

        # 选择单程
        if single_way.is_selected():
            pass
        else:
            single_way.click()

        # 选择到达城市-上海
        action = ActionChains(self.driver)
        time.sleep(5)
        action.move_to_element(to_city).click().perform()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "//div[@data-panel='domesticto-flight-hotcity-to']//a[@class='js-hotcitylist' and text()='上海']").click()
        time.sleep(5)

        # 选择出发城市-北京
        action.move_to_element(from_city).click().perform()
        time.sleep(5)
        self.driver.find_element_by_xpath(
            "//div[@data-panel='domesticfrom-flight-hotcity-from']//a[@class='js-hotcitylist' and text()='北京']").click()
        # self.driver.implicitly_wait(8)
        time.sleep(5)

        # 设置出发日期-7天后
        date = (datetime.datetime.now() + datetime.timedelta(days=7)).strftime("%Y-%m-%d")
        from_date.send_keys(Keys.CONTROL + "a")  # ctrl+a 全选
        time.sleep(5)
        from_date.send_keys(date)

        # 搜索
        self.driver.find_element_by_xpath('//*[@id="dfsForm"]/div[4]/button').click()


if __name__ == '__main__':
    unittest.main()
