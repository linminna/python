
# 异常捕捉 try-except-else-finally
# 异常抛出 raise

try:
    a = "异常测试"
    print(a)
    # open("a.txt", "r")
except NameError as msg:
    print("--error--" + msg)
else:
    print("--else--")
finally:
    print("--finally--")


def say_hello(name=None):
    if name is None:
        raise NameError("'name' can not be empty!")
    else:
        print("hello, %s" % name)


say_hello("lmn")
say_hello()
