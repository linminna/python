from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

# 1、driver.back()  driver.refresh()  driver.forward()
# 2、ActionChains(driver).move_to_element(above).perform()  鼠标操作
# 3、Path(imagePath).is_dir()  判断文件夹是否存在
# 4、driver.save_screenshot(imagePath + "/news.png")  截屏
# 5、find_element_by_link_text 根据文字定位
# 6、driver.get_cookies() 获取当前所有cookies.
# 7、driver.add_cookie({"name": "lmn", "value": "123"})  添加cookie
# 8、get_cookie(name)  返回cookie字典中key为 name 的Cookie
# 9、delete_cookie(name, optionStr)  删除name名为optionStr的的Cookie

driver = webdriver.Chrome()
driver.set_window_size(800, 600)

first_url = "https://www.baidu.com"
print("now access %s" % first_url)
driver.get(first_url)

sleep(1)
second_url = "https://news.baidu.com"
print("now access %s" % second_url)
driver.get(second_url)

sleep(3)
print("back to %s" % first_url)
driver.back()

sleep(3)
# 页面刷新
driver.refresh()
above = driver.find_element_by_link_text("设置")
# 将鼠标移至元素上，在调用时需要指定元素
# context_click() 右击  drag_and_drop() 拖动
ActionChains(driver).move_to_element(above).perform()

sleep(3)
print("forward to %s" % second_url)
driver.forward()

sleep(3)
imagePath = "D:/python-workspace/images"
if Path(imagePath).is_dir():  # 判断文件夹路径是否已经存在
    pass
else:
    print("mkdir--" + imagePath)
    Path(imagePath).mkdir()
    driver.save_screenshot(imagePath + "/news.png")

driver.add_cookie({"name": "lmn", "value": "123"})
cookies = driver.get_cookies()
for cookie in cookies:
    print("%s -> %s" % (cookie['name'], cookie['value']))

print(driver.get_cookie('lmn'))
print('success')
driver.quit()
