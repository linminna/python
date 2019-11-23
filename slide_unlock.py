from time import sleep

from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver import ActionChains

# 运行结果不太明显
# ActionChains是自动执行低级交互的一种方式，例如：鼠标移动，鼠标点按，键盘操作，文本操作等
# click_and_hold()  按住鼠标左键在源元素上，点击并且不释放
# move_by_offset(xoffset, yoffset)  鼠标从当前位置移动到某个坐标
# click_and_hold(on_element=None)  点击鼠标左键，不松开
# context_click(on_element=None)   点击鼠标右键
# double_click(on_element=None)   双击鼠标左键
# drag_and_drop(source, target)   拖拽到某个元素然后松开
# drag_and_drop_by_offset(source, xoffset, yoffset)   拖拽到某个坐标然后松开
# perform()  执行链中的所有动作

driver = webdriver.Chrome()
driver.get("https://www.helloweba.net/demo/2017/unlock/")

slide = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]
action = ActionChains(driver)
action.click_and_hold(slide).perform()

for index in range(200):
    try:
        print(index)
        action.move_by_offset(8, 0).perform()
    except UnexpectedAlertPresentException:
        # driver.switch_to.alert.accept()
        break
    else:
        action.reset_actions()
        sleep(0.1)

text = driver.switch_to.alert.text
print(text)

driver.quit()
