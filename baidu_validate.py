from time import sleep

from selenium import webdriver

# 获得验证信息
# 1、driver.current_url  driver.title
# 2、find_element_by_class_name
# 3、set_window_size 设置浏览器窗口大小
# 4、driver.execute_script(js)  执行js脚本

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
print("before search...")
title = driver.title
current_url = driver.current_url
print("title:" + title + ", current_url:" + current_url)

driver.set_window_size(800, 600)
driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
sleep(5)

print("after search...")
title = driver.title
current_url = driver.current_url
print("title:" + title + ", current_url:" + current_url)

num = driver.find_element_by_class_name("nums").text
print("result:\n" + num)

# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100, 450);"
driver.execute_script(js)

sleep(5)
driver.quit()
