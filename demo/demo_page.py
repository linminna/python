from poium import Page, PageElement


class DemoPage(Page):
    single_way = PageElement(xpath='//*[@id="searchTypeSng"]')
    from_city = PageElement(xpath='//*[@id="dfsForm"]/div[2]/div[1]/div/input')  # 出发城市
    to_city = PageElement(xpath='//*[@id="dfsForm"]/div[2]/div[2]/div/input')  # 到达城市
    from_date = PageElement(xpath='//*[@id="fromDate"]')  # 出发时间
