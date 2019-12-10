class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url=None):
        if url is None:
            self.driver.get(self.url)
        else:
            self.driver.get(url)

    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)
