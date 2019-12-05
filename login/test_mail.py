from time import sleep

from selenium import webdriver

from user_login import *

# 1、模块化与参数化
# 2、如无法引入同目录下的py文件时，则需要将上级目录mark as source
#    注：最好先进行变更 然后再进行编写模块化的py文件
# 3、定位动态ID  driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
# 4、存在iframe的，必须先切换 driver.switch_to.frame

driver = webdriver.Chrome()
driver.get("http://www.126.com")

mail = Mail(driver)
mail.login("111", "222")

sleep(3)
print("====success====")
driver.quit()
