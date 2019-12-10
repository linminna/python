from time import sleep

from selenium.webdriver import Remote, DesiredCapabilities

# grid2 不提供单独的jar包，已集成至 selenium server中
# 下载运行即可  https://selenium.dev/downloads/  selenium-server-standalone-x.xxx.xx.jar
# desired_capabilities 用于定义运行的浏览器、版本、平台等信息，这里必须定义，否则将会报错 SessionNotCreatedException
# 此处 引用Chrome浏览器

driver = Remote(desired_capabilities=DesiredCapabilities.CHROME.copy())
driver.get("http://www.baidu.com")
sleep(3)
driver.quit()

# 自动化执行过程
# 1、selenium Remote()
# 2、Grid hub节点  --》 Grid node节点  --》 chromedriver驱动 --》 启动浏览器（生成sessionId）
# 3、driver.quit() 在执行时删除相应的 sessionId
