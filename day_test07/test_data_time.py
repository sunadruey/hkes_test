from day_test07.test_browser import Base
from time import sleep

class TestData(Base):

    def testdate(self):
        self.driver.get('https://www.12306.cn/index/')
        self.driver.execute_script('a=document.getElementById("train_date");a.removeAttribute("readonly")')
        self.driver.execute_script("document.getElementById('train_date').value='2021-05-27'")
        sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value")
