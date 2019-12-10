from base_page import BasePage


# 百度page层，获取页面上的元素
class BaiduPage(BasePage):
    
    def search_input(self, search_key):
        self.by_id("kw").send_keys(search_key)

    def search_button(self):
        self.by_id("su").click()
