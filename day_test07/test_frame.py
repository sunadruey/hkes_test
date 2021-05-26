from selenium import  webdriver

from day_test07.test_window_base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to_frame('iframeResult')
        self.driver.find_element_by_id('draggable').text
        self.driver.switch_to.parent_frame()
        # self.driver.switch_to.default_content() 等价的切换
        self.driver.find_element_by_id('submitBTN').text

#         不在frame下 切回原页面




