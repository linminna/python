import os
from time import sleep

from selenium import webdriver

# 1、profile.default_content_settings.popups：0 为屏蔽弹窗，1 为开启弹窗  暂时没观察到明显区别
# 2、download.default_directory：指定下载文件存放路径
# 3、webdriver.ChromeOptions() 获取参数
# 4、options.add_experimental_option("prefs", prefs) 设置参数
# 5、driver = webdriver.Chrome(chrome_options=options) 使用参数
# 6、os.getcwd() 获取当前文件的路径

options = webdriver.ChromeOptions()
prefs = {
    'profile.default_content_settings.popups': 1,
    'download.default_directory': os.getcwd()
}
print("os.getcwd()--" + os.getcwd())
options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=options)

driver.get("https://pypi.org/project/selenium/#files")
driver.find_element_by_link_text("selenium-3.141.0.tar.gz").click()
sleep(60)
driver.quit()
