import unittest

# 一次性执行多个测试文件, 指定扫描目录 及 设置规则pattern
# unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
# 备注：此处执行将会扫描到 所有继承unittest.TestCase，并以test开头的测试文件

test_dir = ""
suits = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suits)
