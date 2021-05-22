#test.py
import pytest

def setup_module():
    print('setup_module:整个.py模块只执行一次')

def teardown_module():
    print('teardown_module:整个.py模块只执行一次')

def setup_function():
    print('setup_function:每个用例开始前都会执行')

def teardown_function():
    print('teardown_function:每个用例结束后都会执行')

def test_one():
    print('正在执行----test_one')
    assert (1,2) == (1,2)

def test_two():
    print('正在执行----test_two')
    assert (1,2) == (1,2)

def test_three():
    print('正在执行----test_three')
    assert (1,2) == (1,2)

if __name__ == '__main__':
    pytest.main(['-s','test.py'])
