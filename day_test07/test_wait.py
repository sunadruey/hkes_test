import selenium
from selenium import webdriver
import  time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome(executable_path="/Users/yuanbao/Downloads/chromedriver")
        self.driver.get("https://ceshiren.com/categories")
        self.driver.implicitly_wait(3)


    def test_wait(self):
        time.sleep(3)
        self.driver.find_element_by_xpath("//*[text()='所有分类']").click()
        time.sleep(3)

        # def wait(x):
        #     return len(self.driver.find_element_by_xpath('category-name'))>=1


        WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(( By.XPATH ,"//*[@class='category-text-title']")))
        self.driver.find_element_by_xpath("//*[(@title='在最近的一年，一月，一周或一天最活跃的话题')]").click()