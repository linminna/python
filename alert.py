from time import sleep

from selenium import webdriver

# 弹框 driver.switch_to_alert()

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

sleep(3)
driver.find_element_by_link_text("设置").click()
sleep(3)
driver.find_element_by_link_text("搜索设置").click()

sleep(3)
driver.find_element_by_link_text("保存设置").click()

# 相当于操作句柄 切换至弹框
alert = driver.switch_to_alert()
alertText = alert.text;
print("alertText: " + alertText)

sleep(3)

# 相当于点击弹框上的 确认按钮
alert.accept()
sleep(3)
driver.quit()
