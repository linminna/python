from calculator import Calculator


# 当其中某个方法执行失败后 后面的测试函数将不再执行

def test_add():
    c = Calculator(1, 1)
    num = c.add()
    assert num == 2, 'add出错'


def test_sub():
    c = Calculator(1, 1)
    num = c.sub()
    assert num == 0, 'sub出错'


def test_mul():
    c = Calculator(1, 1)
    num = c.mul()
    assert num == 0, 'mul出错'


def test_div():
    c = Calculator(1, 1)
    num = c.div()
    assert num == 1, 'div出错'


if __name__ == '__main__':
    test_add()
    test_sub()
    test_mul()
    test_div()
