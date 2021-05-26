import selenium
from selenium import  webdriver
from selenium.webdriver import TouchActions
import  time


class TestActionTouch:

    def  setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(executable_path="/Users/yuanbao/Downloads/chromedriver",chrome_options=opt)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction_scrollballbtton(self):
        self.driver.get("https://www.baidu.com/")
        ele_b=self.driver.find_element_by_id("kw")
        ele_search=self.driver.find_element_by_id("su")
        ele_b.send_keys("selenium测试")
        action=TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()
        action.scroll_from_element(ele_b,0,10000).perform()
        time.sleep(10)


