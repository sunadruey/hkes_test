import  selenium
from selenium import  webdriver
from selenium.webdriver import ActionChains
import time
import pytest
from selenium.webdriver.common.keys import Keys


class TestActionChains():

    def setup(self):
        self.driver=webdriver.Chrome(executable_path="/Users/yuanbao/Downloads/chromedriver")


    def tearDown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_lick(self):
        self.driver.get("https://www.baidu.com/")
        element=self.driver.find_element_by_id('kw')
        action = ActionChains(self.driver)
        action.send_keys("肖战")
        action.perform()

    @pytest.mark.skip
    def test_case_move_element(self):
        self.driver.get("https://www.baidu.com/")
        ele=self.driver.find_element_by_id('s-usersetting-top')
        time.sleep(3)
        action= ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()


    def test_case_key(self):
        self.driver.get("https://www.baidu.com/")
        ele=self.driver.find_element_by_id('kw')
        time.sleep(3)
        action= ActionChains(self.driver)
        action.send_keys("肖战").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("王一博").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        time.sleep(3)





