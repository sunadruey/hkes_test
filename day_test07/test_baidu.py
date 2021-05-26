import selenium
from selenium import webdriver
import  time




class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome(executable_path="/Users/yuanbao/Downloads/chromedriver")
        self.driver.get("https://www.baidu.com/")
        self.driver.implicitly_wait(3)


    def test_wait(self):

        # self.driver.find_element_by_xpath("//*[@id='kw']").send_keys("霍格沃兹测试学院")
        # self.driver.find_element_by_id('kw').send_keys("霍格沃兹测试学院")
        self.driver.find_element_by_css_selector('[id=kw]').send_keys("霍格沃兹测试学院")
        self.driver.find_element_by_id('su').click()



