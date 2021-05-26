import selenium
from selenium import webdriver
from time import sleep
from selenium import webdriver

from selenium.webdriver.common.by import By


class TestHogwars():

    def setup(self):
        self.driver = webdriver.Chrome(executable_path="/Users/yuanbao/Downloads/chromedriver")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_hogwars(self):
        self.driver.get('https://testerhome.com/')
        sleep(5)
        self.driver.find_element_by_link_text("社团").click()
        sleep(5)
        self.driver.find_element_by_link_text("求职面试圈").click()
        sleep(5)
        self.driver.find_element(By.CSS_SELECTOR ,".topics/29703 .node").click()

        # self.driver.find_element_by_css_selector(".topics/29703 .node").click()
        sleep(5)
