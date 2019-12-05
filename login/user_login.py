class Mail:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        # 登录
        self.driver.find_element_by_class_name("new-loginFunc").click()
        # x-URS-iframe  'x-URS-iframe1574476803543.1255'  定位动态ID
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//iframe[starts-with(@id, 'x-URS-iframe')]"))

        # self.driver.find_element_by_name("email") 可直接定位
        self.driver.find_element_by_name("email").clear()
        self.driver.find_element_by_xpath("//input[@type='text' and @name='email']").send_keys(username)
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send_keys(password)
        self.driver.find_element_by_id("dologin").click()

    def logout(self):
        # 退出
        self.driver.find_element_by_link_text("退出").click()