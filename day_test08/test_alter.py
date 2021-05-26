from time import sleep

from selenium.webdriver import ActionChains

from day_test08.Base import Base


class TestAlter(Base):
    def test_alter(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to_frame("iframeResult")
        drag=self.driver.find_element_by_id('draggable')
        drop=self.driver.find_element_by_id('droppable')
        action=ActionChains(self.driver)
        action.drag_and_drop(drag,drop).perform()
        sleep(3)
        print("点击 alter 确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        self.driver.find_element_by_id('submitBTN').click()

        sleep(4)