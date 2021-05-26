from day_test07.test_window_base import Base
from time import sleep

class TestWindows(Base):
    def test_login(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element_by_id('s-top-loginbtn').click()
        print(self.driver.current_window_handle)
        self.driver.find_element_by_link_text("立即注册").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows=self.driver.window_handles
        self.driver.switch_to_window(windows[-1])

        self.driver.find_element_by_id('TANGRAM__PSP_4__userName')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone')
        sleep(4)
        self.driver.switch_to_window(windows[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys("usernaem-1")
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys("userpaasword")
        self.driver.find_element_by_id("TANGRAM__PSP_11__submit").click()
        sleep(2)





