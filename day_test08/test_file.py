from  selenium import  webdriver
from time import sleep
from day_test08.Base import Base


class TestFIle(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id("uploadImg").send_keys('/Users/yuanbao/PycharmProjects/hkes_test/image/肖战.jpeg')
        sleep(4)



