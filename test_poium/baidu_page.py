from poium import Page, PageElement


# Page Object 一种设计模式
# 其中，PageObject对应页面对象，PageModules对应页面内容
# 不需要自己管理浏览器
# 在运行时选择浏览器，而不是类级别
# 不需要直接接触selenium

# 百度page层，获取页面上的元素
class BaiduPage(Page):

    def __init__(self, driver):
        self.driver = driver

    search_input = PageElement(id_="kw", timeout=5, describe="搜索内容")
    search_button = PageElement(id_="su")

    # elem_name = PageElement(name="")
    # elem_class = PageElement(class_name="")
    # elem_tag = PageElement(tag="")
    # elem_link_text = PageElement(link_text="")
    # elem_css = PageElement(css="#id")
    # 也支持 partial_link_text 与 xpath 定位方式
    # 通过timeout设置元素超时时间，默认为10s  PageElement(id_="kw", timeout=5)
    # 给元素增加注释  PageElement(id_="su", describe="搜索按钮")
