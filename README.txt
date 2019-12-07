selenium只支持java8 以上版本，ie9.0版本以上
appium 移动端的selenium自动化测试工具，支持ios和安卓平台上的原生应用、web应用和混合应用。
       它是一个跨平台的测试工具，可在不同平台使用同一套api编写的自动化测试脚本，提高了复用性。


---------------------------------------------------------------------------------------------------------

涉及到的安装命令：
最新的python安装程序已经集成pip(pip install xx / pip uninstall xx / pip show xx)，可进行管理相关第三方库。

selenium安装： pip install selenium
pip命令升级： python -m pip --default-timeout=100 install --upgrade pip
邮件发送：   pip install yagmail
unittest框架：参数化库     pip install parameterized、 pip install ddt
              读取yml文件  pip install pyyaml
pytest第三方测试框架：  pip install pytest
                pip install pytest-rerunfailures  测试用例的重试机制
                pip install pytest-parallel   测试用例的并行运行

---------------------------------------------------------------------------------------------------------

# 异常捕捉 try-except-else-finally
# 异常抛出 raise

---------------------------------------------------------------------------------------------------------
在使用selenium之前，需要下载对应的浏览器驱动，可将其放在python安装目录的/Scripts下面


selenium元素定位及动作
定位： id、name、class、tag、link_text、partial link（部分文字定位）、XPath、CSS_selector

# 1、driver.back()  driver.refresh()  driver.forward()
# 2、ActionChains(driver).move_to_element(above).perform()  鼠标操作
# 3、Path(imagePath).is_dir()  判断文件夹是否存在
# 4、driver.save_screenshot(imagePath + "/news.png")  截屏
# 5、find_element_by_link_text 根据文字定位
     find_element_by_link_xpath("//form[@id='']/span[2]/input")
     find_element_by_link_xpath("//span[contains(@class, '')]/input")
     find_element_by_link_xpath("//a[contains(text(), '一个很长的text')]")
     find_element_by_css_selector("form.fm > span > input.s_ipt")   class属性为 fm 的form标签下的 span 标签下 class属性为s_ipt的input标签

# 6、driver.get_cookies() 获取当前所有cookies.
# 7、driver.add_cookie({"name": "lmn", "value": "123"})  添加cookie
# 8、get_cookie(name)  返回cookie字典中key为 name 的Cookie
# 9、delete_cookie(name, optionStr)  删除name名为optionStr的的Cookie

# 弹框 driver.switch_to_alert()

# 获得验证信息
# 1、driver.current_url  driver.title
# 2、find_element_by_class_name
# 3、set_window_size 设置浏览器窗口大小
# 4、driver.execute_script(js)  执行js脚本


# 1、driver.implicitly_wait(5) 隐式等待，不影响脚本的执行时间
#    当脚本中存在定位元素的操作时，若元素不存在，将会一直轮询，若在规定时间5s内未找到将抛出异常，反之找到的话将会继续往下执行
#    显示等待。。。
# 2、获取当前的窗口句柄 driver.current_window_handle
# 3、获取当前所有窗口句柄 driver.window_handles
# 4、窗口/页面切换 driver.switch_to.window(handle)
# 5、关闭当前窗口 driver.close()
# 6、关闭浏览器 driver.quit()


# 1、模块化与参数化
# 2、如无法引入同目录下的py文件时，则需要将上级目录mark as source
#    注：最好先进行变更 然后再进行编写模块化的py文件
# 3、定位动态ID  driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]")
# 4、存在iframe的，必须先切换 driver.switch_to.frame


# 1、profile.default_content_settings.popups：0 为屏蔽弹窗，1 为开启弹窗  暂时没观察到明显区别
# 2、download.default_directory：指定下载文件存放路径
# 3、webdriver.ChromeOptions() 获取参数
# 4、options.add_experimental_option("prefs", prefs) 设置参数
# 5、driver = webdriver.Chrome(chrome_options=options) 使用参数
# 6、os.getcwd() 获取当前文件的路径

# webdriver.TouchActions(driver)  实现下拉操作
# scroll_from_element(year, 0, 5).perform()  操作元素 x偏移量  y偏移量
# 报错 WebDriverException: Message: unknown command: Cannot call non W3C standard c


鼠标动作
from selenium.webdriver import ActionChains
# ActionChains 是自动执行低级交互的一种方式，例如：鼠标移动，鼠标点按，键盘操作，文本操作等
# click_and_hold()  按住鼠标左键在源元素上，点击并且不释放
# move_by_offset(xoffset, yoffset)  鼠标从当前位置移动到某个坐标
# click_and_hold(on_element=None)  点击鼠标左键，不松开
# context_click(on_element=None)   点击鼠标右键
# double_click(on_element=None)   双击鼠标左键
# drag_and_drop(source, target)   拖拽到某个元素然后松开
# drag_and_drop_by_offset(source, xoffset, yoffset)   拖拽到某个坐标然后松开
# perform()  执行链中的所有动作


# 读取各种类型的文件 .json  .txt  .csv
# 注意：谨防重名导致导入失败，不要将文件命名为 json.py
# as 可用于起别名
# json.loads(data) 将字符串转化为json格式
# read() 读取整个文件  readline()读取一行数据   readlines()读取所有行的数据
# a[::-1]  字符串反转
# a[:-1]   从位置0到位置-1之前的数,最后一个位置为-1.
# b = a[i:j]   表示复制a[i]到a[j-1]，以生成新的list对象  当i,j都缺省时，a[:]就相当于完整复制一份a
# 读取csv文件 谨防 中文乱码 + 表头
# csv.reader(codecs.open("./file/user_info.csv", "r", "gbk"))  codecs 是python编解码器，此处指定gbk
# islice(data, 0, None)   Python 提供的 itertools 工具，可在读取数据时从指定行开始，提高了一定的循环效率


# You are using pip version 18.1, however version 19.3.1 is available.
# pip升级，python -m pip --default-timeout=100 install --upgrade pip
# pip命令升级才能使用pip install yagmail
# 此处，pip升级失败，故 邮件发送暂时未完成
# 连接邮箱服务器
# 邮件正文、主题、内容的写入
# 邮件发送

# 调用js 播放视频

---------------------------------------------------------------------------------------------------------
# 一次性执行多个测试文件, 指定扫描目录 及 设置规则pattern
# unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
# 备注：此处执行将会扫描到 所有继承unittest.TestCase，并以test开头的测试文件

# 1、类方法的使用
# 2、模块化、参数化
# 3、单元测试框架
# 安装parameterized、ddt  pip install
# 4、@parameterized([]) 参数化库的使用
# 5、@ddt注意在类上添加，否则在运行时会报错
# @data(("a1", "a11"), ("a2", "a22"))
#     @unpack
# 如果没有unpack，那么[a1,a11] 当成一个参数传入用例运行
# 如果有unpack，那么[a1,a11] 被分解开，按照用例中的两个参数传递
# 读取json文件作为参数列表  @file_data(parent_path + './file/ddt_data.json')
# 若要读取yml文件，需要先 pip install pyyaml，注意：此处开始安装时失败，后面在将pip升级后 安装成功。
# 获取当前文件的父目录  os.path.dirname(os.path.dirname(__file__))
# 当前文件所在目录  os.path.dirname(__file__)


# def setUpModule():  在整个模块的开始执行
# @classmethod   用于类方法上
#     def setUpClass(cls):  在测试类开始和结束时执行

# def setUp(self):  前置方法,在该类中以test开头的方法（测试用例）前后都会被执行
# @unittest.skip("直接跳过测试")  跳过该测试方法的执行


# 测试用例规则：
# 1、创建测试类，并继承 unittest.TestCase
# 2、创建测试方法，必须以 test 开头
# 测试用例前置、后置动作
# suit = unittest.TestSuite()  测试套件（用于测试一组测试用例）
# suit.addTest(TestCalculator("test_add")) addTest可用于调整方法的执行顺序，默认是按照方法名称的ascii码先后顺序来执行
# runner = unittest.TextTestRunner()  测试运行器，可用于执行 runner.run(suit)

---------------------------------------------------------------------------------------------------------

# Page Object 一种设计模式
# 其中，PageObject对应页面对象，PageModules对应页面内容
# 不需要自己管理浏览器
# 在运行时选择浏览器，而不是类级别
# 不需要直接接触selenium

# 注意：使用存在部分问题
# page = BaiduPage(self.driver)
# page.get("https://www.baidu.com")   报错
# 此处获取的page元素 无法调用click()等方法

---------------------------------------------------------------------------------------------------------

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

---------------------------------------------------------------------------------------------------------

Selenium 三大组件 selenium webdriver + selenium ide + selenium grid
Selenium Grid 分布式执行测试
解决重复执行测试、解决多浏览器兼容这是UI自动化的价值

# desired_capabilities 用于定义运行的浏览器、版本、平台等信息，这里必须定义，否则将会报错 SessionNotCreatedException










