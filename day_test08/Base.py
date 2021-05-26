from selenium import webdriver

class Base:
    def setup(self):
        self.driver = webdriver.Chrome(executable_path="/Users/yuanbao/Downloads/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()