import allure
import pytest
TEST_CASE_LINK='https://www.baidu.com/'

@allure.testcase(TEST_CASE_LINK,'百度')
def test_with_testcase_link():
    pass

@pytest.mark
def test_with_testcase_link2():
    pass
