import time

import selenium
from selenium import webdriver

class TestForm:

    def setup(self):
        self.driver = webdriver.Chrome(executable_path="/Users/yuanbao/Downloads/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)


    def teardown(self):
        self.driver.quit()

    def test_login(self):

        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id('user_login').send_keys("username")
        self.driver.find_element_by_id('user_password').send_keys('123456')
        self.driver.find_element_by_xpath('//label[@class="custom-control-label"]').click()
        time.sleep(3)
