from PIL import Image
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

driver.save_screenshot('button.png')
element = driver.find_element_by_id("su")
print(element.location)  # 打印元素坐标
print(element.size)  # 打印元素大小

left = element.location['x']
top = element.location['y']
right = element.location['x'] + element.size['width']
bottom = element.location['y'] + element.size['height']

im = Image.open('button.png')
im = im.crop((left, top, right, bottom))
im.save('button.png')

driver.quit()
