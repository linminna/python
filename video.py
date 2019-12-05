from time import sleep

from selenium import webdriver

# 调用js 播放视频

driver = webdriver.Chrome()
driver.get("http://videojs.com")
video = driver.find_element_by_id("preview-player_html5_api")

# 返回播放文件地址
url = driver.execute_script("return arguments[0].currentSrc;", video)
print(url)

# 开始播放视频
print("===play===")
driver.execute_script("arguments[0].play()", video)

# 假设播放10s
sleep(10)

# 暂停播放
print("===pause===")
driver.execute_script("arguments[0].pause()", video)

print("===end===")
driver.quit()
