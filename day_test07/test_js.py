import  selenium

from day_test07.test_browser import Base
from time import sleep

class TestJs(Base):
    def test_js(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element=self.driver.execute_script("return document.getElementById('su')")
        element.click()
        self.driver.execute_script("document.documentElement.scrollTop=100000")
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[10]").click()
        sleep(4)

        # for code in [
        #
        #     'return document.title',
        #     'return JSON.stringify(performance.timing)'
        #
        # ] :
        #     print(self.driver.execute_script(code))

        self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)")



