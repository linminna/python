from time import sleep

from selenium.webdriver import Remote, DesiredCapabilities

# desired_capabilities 用于定义运行的浏览器、版本、平台等信息，这里必须定义，否则将会报错 SessionNotCreatedException
# 此处 引用Chrome浏览器
driver = Remote(desired_capabilities=DesiredCapabilities.CHROME.copy())
driver.get("http://www.baidu.com")
sleep(3)
driver.quit()
