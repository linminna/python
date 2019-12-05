import time
import unittest

from HTMLTestRunner import HTMLTestRunner

# 一次性执行多个测试文件, 指定扫描目录 及 设置规则pattern
# unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
# 备注：此处执行将会扫描到 所有继承unittest.TestCase，并以test开头的测试文件

test_dir = ""
suits = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    timeStr = time.strftime("%Y_%m_%d_%H_%M_%S")
    # fp = open("./report/" + timeStr + "_result.html", "wb")
    fp = open("./report/result.html", "wb")
    runner = HTMLTestRunner(stream=fp, title='百度搜索测试报告', description='运行')
    runner.run(suits)
    fp.close()
