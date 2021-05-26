import  selenium
from selenium import webdriver


def test_selenium():
    # driver=webdriver.Chrome()
    driver = webdriver.Chrome(executable_path="/Users/yuanbao/Downloads/chromedriver")
    driver.get('https://www.baidu.com/')