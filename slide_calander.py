from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 运行结果不太明显
# webdriver.TouchActions(driver)  实现下拉操作
# scroll_from_element(year, 0, 5).perform()  操作元素 x偏移量  y偏移量
# 报错 WebDriverException: Message: unknown command: Cannot call non W3C standard c

option = Options()
option.add_experimental_option('w3c', False)
driver = webdriver.Chrome(options=option)
driver.get("http://www.jq22.com/yanshi4976")
sleep(2)

driver.switch_to.frame("iframe")
driver.find_element_by_id("appDate").click()

dwwos = driver.find_elements_by_class_name("dwwo")
for dwwo in dwwos:
    print(dwwo)
year = dwwos[0]
month = dwwos[1]
day = dwwos[2]

action = webdriver.TouchActions(driver)
action.scroll_from_element(year, 0, 2).perform()
action.scroll_from_element(month, 0, 2).perform()
action.scroll_from_element(day, 0, 2).perform()

sleep(30)
driver.quit()
