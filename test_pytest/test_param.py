import logging
import math

import pytest


# pytest 第三方单元测试框架

# 没有main方法，不能直接运行 只能通过命令行执行 > pytest -v ./test_pytest/test_param.py
# 添加main方法执行
# pytest -k add test_param.py 运行名称中包含add字符串的测试用例
# -q: 安静模式, 不输出环境信息
# -v: 丰富信息模式, 输出更详细的用例执行信息
# -s: 显示程序中的print/logging输出
# 默认情况下，logging将日志打印到屏幕，日志级别为WARNING；
# 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
# 设置日志级别 logging.basicConfig(level=logging.INFO)
# pytest用logging和 pytest -s（pytest --capture=no）实现实时输出log信息

# pytest ./test_pytest/test_param.py --pastebin=all  生成测试报告链接，可点击查看详细
# pytest ./test_pytest/test_param.py --html=./test_pytest/report/result.html  生成html格式的测试报告，须要先 pip install pytest-html
# pip install pytest-rerunfailures 可在测试用例失败时进行重试
# pytest -v ./test_pytest/test_rerunfailure.py --reruns 3  测试用例失败后可重试三次

# 标记用例执行顺顺序pytest.mark.run(order=1) (需安装pytest-ordering)

# @pytest.fixture()装饰器用于声明函数是一个fixture。  如果测试函数的参数列表中包含fixture名，那么pytest会检测到，并在测试函数运行之前执行fixture。
# 其中，参数scope，默认function， 也可赋值class、module、session

# pip install pytest-parallel 可实现测试用例的并行运行（在执行过程可能产生干扰，请谨慎使用）

@pytest.mark.parametrize(
    "base, exponent, expected", [(2, 2, 4), (2, 3, 8), (2, 4, 16)], ids=["case22", "case23", "case24"]
)
@pytest.mark.run(order=1)
def test_pow(base, exponent, expected):
    assert math.pow(base, exponent) == expected


logging.basicConfig(level=logging.INFO)


# 目前只会在 test_baidu() 出错时 打印print语句
@pytest.fixture()
def test_url():
    logging.info("=====打印 test_url 装饰器函数=====")
    return "www.baidu.com"


def test_baidu(test_url):
    logging.info("--test_baidu--" + test_url)
    assert test_url == "www.baidu.com"


# 在测试用例失败时进行重试
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_fail_rerun():
    assert 2 + 4 == 6


if __name__ == '__main__':
    # pytest.main(['-svq'])  通过数组指定多个参数
    pytest.main(['-s'])
