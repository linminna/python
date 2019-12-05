from time import sleep

from selenium import webdriver

# 1、driver.implicitly_wait(5) 隐式等待，不影响脚本的执行时间
#    当脚本中存在定位元素的操作时，若元素不存在，将会一直轮询，若在规定时间5s内未找到将抛出异常，反之找到的话将会继续往下执行
#    显示等待。。。
# 2、获取当前的窗口句柄 driver.current_window_handle
# 3、获取当前所有窗口句柄 driver.window_handles
# 4、窗口/页面切换 driver.switch_to.window(handle)
# 5、关闭当前窗口 driver.close()
# 6、关闭浏览器 driver.quit()

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.implicitly_wait(5)
search_window = driver.current_window_handle
print("search_window:" + search_window)

sleep(3)
driver.find_element_by_link_text("登录").click()
sleep(3)
driver.find_element_by_link_text("立即注册").click()

# 获取当前所有窗口句柄
handles = driver.window_handles
length = handles.__len__()
print("handle-length:%d" % length)
for handle in handles:
    if handle != search_window:
        print("handle:" + handle.title())
        # 切换窗口
        driver.switch_to.window(handle)
        print("title:" + driver.title)
        driver.find_element_by_name("userName").send_keys("name")
        driver.find_element_by_name("phone").send_keys("135xxxxxxxx")
        sleep(5)
        # 关闭当前窗口（页面）
        driver.close()

print("-----handles-end---")
sleep(3)
# 切换至外层窗口
driver.switch_to.window(search_window)
print(driver.title)
sleep(3)
driver.quit()
